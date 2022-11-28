from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Gallery(models.Model):
    """
    Image gallery model.
    """
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="galleries",
                               verbose_name="author")
    image = models.ImageField("image", upload_to="image/")

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
