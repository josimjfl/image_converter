# image_convert/models.py
from django.db import models

class ConvertedImage(models.Model):
    converted_image = models.ImageField(upload_to='converted_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Converted Image {self.id} - {self.converted_image.name}"
