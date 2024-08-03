import abc

from rest_framework.views import APIView


class BaseAPIView(APIView, abc.ABC):
    queryset = None
    serializer_class = None

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    def data_validation(self):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return serializer, serializer.validated_data
