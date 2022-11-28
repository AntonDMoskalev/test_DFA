from drf_extra_fields.fields import Base64ImageField
from images.models import Gallery
from rest_framework import serializers


class GallerySerializers(serializers.ModelSerializer):
    """
    The serializer for the Gallery model:
    1. The Image field receives data in Base64
       format and decodes it into an image.
    2. When creating a gallery, the user is
       automatically added to the user field.
    """
    image = Base64ImageField()
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Gallery
        fields = ("id", "author", "image")

    def create(self, validated_data):
        author = self.context['request'].user
        image = validated_data.pop('image')
        return Gallery.objects.create(author=author, image=image)
