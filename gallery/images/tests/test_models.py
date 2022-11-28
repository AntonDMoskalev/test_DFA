from django.contrib.auth import get_user_model
from django.test import TestCase
from images.models import Gallery

User = get_user_model()


class GalleryModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create(username="test", password="test")
        cls.gallery = Gallery.objects.create(
            author=cls.user,
            image='Тестовый текст',
        )

    def test_verbose_name(self):
        """verbose_name in the fields matches the expected one."""
        task = GalleryModelTest.gallery
        field_verboses = {
            'author': 'author',
            'image': 'image',
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).verbose_name, expected_value)
