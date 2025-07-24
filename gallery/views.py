from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Gallery
from .serializers import GallerySerializer

class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Gallery.objects.all()

    def perform_create(self, serializer):
        stylist = getattr(self.request.user, 'stylist', None)
        stylist = (self.request.user and self.request.user.role == 'stylist') or self.request.user.is_superuser
        if not stylist:
            raise PermissionDenied("You are not a stylist.")
        serializer.save(stylist=stylist)

    def perform_update(self, serializer):
        gallery = self.get_object()
        if self.request.user.is_superuser or gallery.stylist.user == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied("You do not have permission to update this gallery.")

    def perform_destroy(self, instance):
        if self.request.user.is_superuser or instance.stylist.user == self.request.user:
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this gallery.")
