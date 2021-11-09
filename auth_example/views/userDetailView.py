from rest_framework                          import status, generics
from rest_framework.response                 import Response
from rest_framework.permissions              import IsAuthenticated
from rest_framework_simplejwt.backends       import TokenBackend
from django.conf                             import settings

from auth_example.models.user                import User
from auth_example.serializers.userSerializer import UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token         = request.META.get('HTTP_AUTHORIZATION')[7:]
        token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data    = token_backend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            string_response = {'detail': "Acceso no autorizado."}
            return Response(string_response, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(self, request, *args, **kwargs)
