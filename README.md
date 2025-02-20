![Screenshot from 2025-02-20 02-23-22](https://github.com/user-attachments/assets/6d82d82a-e163-4eb8-9f4f-4862c33bac53)# Wizard Portfolio -

## 🧙‍♂️ Project Overview
Wizard Portfolio is a **sci-fi, wizard-themed** developer portfolio built with **Django, HTML, CSS, and JavaScript**. It features a **dark theme with neon colors**, magical animations, and a futuristic Matrix-like aesthetic. Users can explore **projects, blogs, and interact** through likes, comments, and shares.

---

## ✨ Features
- **Wizardly UI** with neon-glowing elements and arcane symbols.
- **User Authentication** (Login, Signup, Password Reset) with enchanted-themed UI.
- **Project Showcase** - Displays projects with images, descriptions, and a magic-styled "Unveil the Secrets" button.
- **Blog Section** - Users can read, like, and comment on blog posts.
- **Social Media Links** - Magically animated icons.
- **Fully Responsive Design** - Works smoothly on all screen sizes.
- **Dark Mode + Neon Accents** for an immersive futuristic feel.
- **Django Backend** - Structured with separate apps (`portfolio`, `blogs`, `projects`, `users`).

---
## Screenshots
![Homepage](static/images/![Screenshot from 2025-02-20 02-17-16](https://github.com/user-attachments/assets/c3469b18-9a35-4894-a09b-b04c838786bf)
)
![projects_page](static/images/![Screenshot from 2025-02-20 02-18-16](https://github.com/user-attachments/assets/d184c5dd-a272-4565-890a-33f0e1b1973b)
)
![project_detail](static/images/![Screenshot from 2025-02-20 02-18-45](https://github.com/user-attachments/assets/05bf45b4-8d17-4120-bdbb-96830965c46a)
)
![project_detail](static/images/![Screenshot from 2025-02-20 02-19-11](https://github.com/user-attachments/assets/d44bac03-09cc-4118-97bb-08c284336f92)
)
![Blogs_page](static/images/![Screenshot from 2025-02-20 02-19-42](https://github.com/user-attachments/assets/2100ef81-a5f5-4052-b07f-e4a2e0912a23)
)
![blog_detail](static/images/![Screenshot from 2025-02-20 02-20-16](https://github.com/user-attachments/assets/33f21c56-3eb2-4a3b-aab7-cee3acfc4256)
)
![Profile](static/images/![Screenshot from 2025-02-20 02-21-05](https://github.com/user-attachments/assets/6c549971-6e63-42e9-98a7-bd715cdcb7a9)
)
![contact](static/images/![Screenshot from 2025-02-20 02-21-41](https://github.com/user-attachments/assets/a50357fc-13dc-414f-9b77-9b634f46ecc8)
)
![about](static/images/![Screenshot from 2025-02-20 02-22-14](https://github.com/user-attachments/assets/90eb2db8-b444-4924-b368-363b9cf2e88d)
)
![about_cont](static/images/![Screenshot from 2025-02-20 02-22-42](https://github.com/user-attachments/assets/3172e31e-3f46-43ed-ac81-c02254879680)
)
![about_cont](static/images/![Screenshot from 2025-02-20 02-23-22](https://github.com/user-attachments/assets/72d9b285-eff5-42af-91a0-4628f27f4026)
)
![Login](static/images/![Screenshot from 2025-02-20 02-30-27](https://github.com/user-attachments/assets/6eed6e7c-8855-4ba1-bdad-fbc859143b26)
)

## 🚀 Installation
### **1️⃣ Clone the Repository**
```bash
 git clone https://github.com/your-username/wizard-portfolio.git
 cd wizard-portfolio
```

### **2️⃣ Set Up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Database (PostgreSQL)**
Make sure PostgreSQL is installed and update `settings.py` with your database credentials.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wizard_portfolio',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### **5️⃣ Apply Migrations**
```bash
python manage.py migrate
```

### **6️⃣ Create Superuser**
```bash
python manage.py createsuperuser
```

### **7️⃣ Run the Server**
```bash
python manage.py runserver
```

---

## 🔮 Project Structure
```
wizard_portfolio/
│── portfolio/       # Handles Home, About, Contact pages
│── blogs/           # Manages Blog Posts
│── projects/        # Handles Project Listings
│── users/           # Authentication & User Management
│── static/          # CSS, JS, Images (Arcane Symbols, Neon Effects)
│── templates/       # HTML Files (Styled with Wizard Aesthetics)
│── media/           # Uploaded Images (Projects & Blogs)
│── manage.py        # Django Management Script
│── requirements.txt # Dependencies
```

---

## 📸 Media & Static Files
For images to load correctly, configure `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```
Run:
```bash
python manage.py collectstatic
```
Ensure **DEBUG=False** in production and set up proper media file handling.

---

## 🌐 Deployment
1. **Set up PostgreSQL on your server.**
2. **Use Gunicorn & Nginx for Django hosting.**
3. **Use `whitenoise` for static files (if needed).**
4. **Configure `ALLOWED_HOSTS` & `CSRF_TRUSTED_ORIGINS`.**

---

## 🤖 Future Enhancements
- Add **AI-powered portfolio analytics**.
- Implement **real-time chat** for inquiries.
- Introduce **3D magical animations**.

---

## 🪄 Author
Developed by **Pi-johns the Code Wizard** 🧙‍♂️✨

📌 **GitHub**: [YourGitHub](https://github.com/your-username)  
📌 **Portfolio**: [YourWebsite](https://yourwebsite.com)  
📌 **LinkedIn**: [YourLinkedIn](https://linkedin.com/in/yourname)  
📌 **Twitter**: [@YourTwitter](https://twitter.com/yourhandle)  

---

🪄 **Unleash the magic and build your own wizardly portfolio!** 🔥🚀


