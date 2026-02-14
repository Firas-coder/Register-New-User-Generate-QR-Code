Register New User & Generate QR Code

This project allows you to register a new user and automatically generate a unique QR Code for that user.

The generated QR code can contain user information such as username, email, or unique ID.

🚀 Features

✅ Register new users

✅ Store user data

✅ Automatically generate QR Code for each user

✅ Save QR Code as an image

✅ Simple and clean structure

🛠️ Technologies Used

🐍 Python

🌐 Django (if used)

📦 qrcode library

🖼️ Pillow (PIL)

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


Or manually:

pip install django qrcode[pil]

▶️ Run The Project
python manage.py runserver


Open your browser and go to:

http://127.0.0.1:8000/

📷 How It Works

User fills out the registration form

Data is saved to the database

A QR Code is generated automatically

QR Code image is stored and linked to the user

📂 Project Structure (Example)
project/
│
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│
├── media/
│   └── qrcodes/
│
├── templates/
│
└── manage.py

📌 Example QR Code Generation (Python)
import qrcode

data = f"Username: {user.username} | Email: {user.email}"

qr = qrcode.make(data)
qr.save(f"media/qrcodes/{user.username}.png")

👨‍💻 Author

Developed by ZeroPyteCode S

🔗 GitHub: https://github.com/Firas-coder)

username : admin
password : 1234
