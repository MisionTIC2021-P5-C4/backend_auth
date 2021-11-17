from rest_framework                          import status, generics
from django.conf                             import settings

from auth_example.models.user                import User
from auth_example.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)


class UserUpdateView(generics.UpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def update(self, request, *args, **kwargs):
        return super().update(self, request, *args, **kwargs)


class UserDeleteView(generics.DestroyAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    def delete(self, request, *args, **kwargs):
        return super().destroy(self, request, *args, **kwargs)