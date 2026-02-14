
# models.py
from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files import File
from PIL import Image
import qrcode
from qrcode.constants import ERROR_CORRECT_L

class UserQRCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes_img/', blank=True)

    def __str__(self):
        return f"QR for {self.user.username}"
