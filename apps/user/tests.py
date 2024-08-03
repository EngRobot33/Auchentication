from django.core.cache import cache
from django.test import TestCase
from rest_framework.reverse import reverse

from apps.user.models import User


class AuchenticationTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.all().delete()
        cache.clear()
        pass

    def test_check_phone_number(self):
        response = self.client.post(reverse('user:check-phone-number'), data={'phone_number': "09123456789"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'detail': 'OK',
            'code': 200,
            'error': None,
            'data': {
                'link': '/api/user/otp-verify/'
            },
        })
        User.objects.create(phone_number='09123456788')

        response = self.client.post(reverse('user:check-phone-number'), data={'phone_number': "09123456788"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'detail': 'OK',
            'code': 200,
            'error': None,
            'data': {
                'link': '/api/user/login/'
            },
        })

    def test_otp_verify(self):
        response = self.client.post(reverse('user:otp-verify'), data={'phone_number': "09123456789", 'otp': 1})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'detail': 'Otp expired',
            'code': 400,
            'data': {},
            'error': None
        })

        self.client.post(reverse('user:check-phone-number'), data={'phone_number': "09123456789"})
        otp = int(cache.get('09123456789'))
        self.assertTrue(otp)
        self.assertEqual(int, type(otp))
        cache.set('09123456789', otp, 100)
        response = self.client.post(reverse('user:otp-verify'), data={'phone_number': "09123456789", 'otp': otp})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {
            'detail': 'Created',
            'code': 201,
            'data': {
                'link': '/api/user/register/',
                'tokens': {
                    'access': response.json()['data']['tokens']['access'],
                    'refresh': response.json()['data']['tokens']['refresh']
                },
            },
            'error': None,
        })
        response = self.client.post(
            reverse('user:register'),
            data={"first_name": "John", "last_name": "Doe", "email": "johndoe@django.dev", "password": "ThisIsJohn33@"})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {
            'code': 401,
            'detail': 'Forbidden',
            'data': {},
            'error': None
        })

    def test_login(self):
        user = User.objects.create(
            phone_number='09123456788',
            first_name='John',
            last_name='Doe',
            email='johndoe@django.dev'
        )
        user.set_password('ThisIsJohn33@')
        user.save()
        response = self.client.post(reverse('user:check-phone-number'), data={'phone_number': "09123456788"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'detail': 'OK',
            'code': 200,
            'data':
                {'link': '/api/user/login/'
                 },
            'error': None
        })

        response = self.client.post(reverse('user:login'), data={'phone_number': "09123456788", 'password': 'ThisIsJohn33@'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'detail': 'OK',
            'code': 200,
            'data': {
                'id': 1,
                'username': '',
                'phone_number': '09123456788',
                'first_name': 'John',
                'last_name': 'Doe',
                'tokens': {
                    'access': response.json()['data']['tokens']['access'],
                    'refresh': response.json()['data']['tokens']['refresh']
                }
            },
            'error': None,
            }
        )
        response = self.client.post(reverse('user:login'), data={'phone_number': "09123456788", 'password': '1234'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.json(), {
                'detail': 'Login failed',
                'code': 403,
                'data': {},
                'error': None
            })
        self.client.post(reverse('user:login'), data={'phone_number': "09123456788", 'password': '1234'})
        self.client.post(reverse('user:login'), data={'phone_number': "09123456788", 'password': '1234'})
        self.client.post(reverse('user:login'), data={'phone_number': "09123456788", 'password': '1234'})

        response = self.client.post(reverse('user:login'), data={'phone_number': "09123456788", 'password': '12345'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(
            response.json(), {
                'detail': 'IP blocked',
                'code': 403,
                'data': {},
                'error': None
            }
        )
