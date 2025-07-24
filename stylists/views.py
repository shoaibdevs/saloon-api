# stylists/views.py

from rest_framework import viewsets
from .models import Stylist
from .serializers import StylistSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class StylistViewSet(viewsets.ModelViewSet):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

