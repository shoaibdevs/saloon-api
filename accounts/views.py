from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import UserSerializer, StylistSerializer
from .utils import getRole

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        identifier = request.data.get("identifier")
        password = request.data.get("password")

        if not identifier or not password:
            return Response({'status': False, 'detail': 'Email/Phone and password are required.'})

        try:
            user = User.objects.get(Q(email__iexact=identifier) | Q(phone=identifier), is_active=True)
        except User.DoesNotExist:
            return Response({'status': False, 'detail': 'User does not exist or is inactive.'})

        if not authenticate(request, email=user.email, password=password):
            return Response({'status': False, 'detail': 'Invalid credentials.'})

        role = getRole(user)
        data = (
            StylistSerializer(user.stylist_profile).data
            if role == "Stylist" and hasattr(user, 'stylist_profile')
            else UserSerializer(user).data
        )

        refresh = RefreshToken.for_user(user)
        return Response({
            'status': True,
            'detail': 'Login successful.',
            'role': role,
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
            'data': data
        })
