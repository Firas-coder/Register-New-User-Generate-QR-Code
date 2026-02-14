
# views.py
from django.shortcuts import render, redirect
from .forms import QRUserForm
from .models import UserQRCode
from django.shortcuts import get_object_or_404
#from .decorators import forAdmins,notloggeduser
from django.contrib.auth.forms import UserCreationForm
#نقوم باستيراد مكاتب خاصة بالتحقق والتسجيل الدخول والخروج
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
#نمنع اليوزر من الوصول الى اي صفحة مالم يقوم بعمل لوك ان
from django.contrib.auth.decorators import login_required 
from django.shortcuts import get_object_or_404
from django.contrib import messages
import qrcode
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import base64
# Create your views here.

def index_fun(request):
    return render(request, 'pages/index.html')


#---------------------------RegisterStart--------------------------------#
def generate_qr_base64(data):
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return img_str

def register_user(request):
    if request.method == 'POST':
        form = QRUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            qr_data = f"Username: {user.username}\nEmail: {user.email}"
            qr_code = generate_qr_base64(qr_data)
            messages.success(request, f"created barcode successfully ✅")
            return render(request, 'pages/qr_success.html', {'qr_code': qr_code})
    else:
        form = QRUserForm()
    return render(request, 'pages/register.html', {'form': form})
#-------------------_______%RegisterEnd%_______------------------------#
