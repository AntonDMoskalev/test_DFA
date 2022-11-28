import os
import shutil

from images.models import Gallery
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from gallery.settings import MEDIA_ROOT

from .serializers import GallerySerializers


class GallaryViewSet(viewsets.ModelViewSet):
    """
    Model View Set for GallerySerializers.
    1. Returns a queryset depending on the user role:
       Superuser - all entries Gallery.
       User - Only User entries.
    2. Added a new router address "gallery/delete-all-image/":
       Deletes all entries from the Gallery database.
       Deletes all images from the 'media/image' folder.
    """
    serializer_class = GallerySerializers

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Gallery.objects.all()
        else:
            return Gallery.objects.filter(author=user)

    @action(detail=False,
            methods=["delete"],
            url_path='delete-all-image',
            permission_classes=[permissions.IsAdminUser])
    def delete_all_image(self, request):
        try:
            Gallery.objects.all().delete()
            path = os.path.join(MEDIA_ROOT, 'image')
            shutil.rmtree(path=path, ignore_errors=False, onerror=None)
            return Response("All images have been "
                            "removed from the gallery.",
                            status=status.HTTP_204_NO_CONTENT)
        except Exception:
            return Response("All images have already been "
                            "removed from the gallery.",
                            status=status.HTTP_204_NO_CONTENT)
