# Auchentication

Auchentication is a simple authentication system with the ability to limit suspicious requests.

The user first enters their mobile phone number. If the user has registered before, they are authenticated by entering a password. If not, a 6-digit one-time code is generated and sent to the user via SMS. The user completes registration by entering the code and then provides personal information such as their first name, last name, and email address.

During the login process, if the user enters the wrong mobile number and password three times, or if an incorrect combination of mobile number and password is entered three times from a single IP address, the user is blocked for 1 hour.

During the registration process, if there are three requests for a one-time code from a single IP address but the entered code is incorrect, or if a mobile number is entered incorrectly three times, the user is blocked for 1 hour.

## Installation without Docker

* First of all clone the project:
```console
username@hostname:~$ git clone https://github.com/EngRobot33/Auchentication.git
```
* Enter the project directory:
```console
username@hostname:~$ cd Auchentication
```
* Then, we need a virtual environment you can create like this:
```console
username@hostname:~/Auchentication$ virtualenv venv
```
* Activate it with the command below:
```console
username@hostname:~/Auchentication$ source venv/bin/activate
```
* After that, you must install all the packages in `requirements.txt` file in project directory:
```console
username@hostname:~/Auchentication$ pip install -r requirements.txt
```

* Create a `.env` file, then add your created config:
```python
SECRET_KEY = 'Your secret key generated by https://djecrety.ir'
DEBUG = 'Project debug status'
CACHES_REDIS_HOST = 'The hostname or IP address of the Redis server used for caching.'
REDIS_TIMEOUT = 'The amount of time (in seconds) to wait for a Redis operation to complete before timing out.'
REDIS_KEY_PREFIX = 'A prefix added to Redis keys to avoid collisions with keys used by other applications.'
OTP_EXPIRE_TIME = 'The duration (in seconds) for which a one-time password (OTP) remains valid.'
ACCESS_TOKEN_LIFETIME = 'The period (in seconds) for which an access token is valid before it needs to be refreshed.'
REFRESH_TOKEN_LIFETIME = 'The duration (in seconds) that a refresh token is valid before it expires.'
SLIDING_TOKEN_LIFETIME = 'The period (in seconds) that a sliding token remains valid, extending its lifetime with each use.'
SLIDING_TOKEN_REFRESH_LIFETIME = 'The duration (in seconds) that a sliding refresh token is valid before requiring re-authentication.'
```
**NOTE: Except `SECRET_KEY` and `DEBUG`, rest of them are optional.**

* Enter the following command for migrations:
```console
username@hostname:~/Auchentication$ python3 manage.py migrate
```
* Run the project via this command:
```console
username@hostname:~/Auchentication$ python3 manage.py runserver
```
* Run the command below for tests:
```console
username@hostname:~/Auchentication$ python3 manage.py test

```

## Installation with Docker

* First of all clone the project:
```console
username@hostname:~$ git clone https://github.com/EngRobot33/Auchentication.git
```
* Enter the project directory:
```console
username@hostname:~$ cd Auchentication
```
* Build and run the containers using docker-compose:
```console
username@hostname:~/Auchentication$ sudo docker-compose up --build
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

