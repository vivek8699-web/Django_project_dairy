``
Project Structure
personal-diary-app/
│
├── core/              # Main app
├── templates/         # HTML templates
├── static/           # CSS/JS files
├── db.sqlite3        # Database
├── manage.py
└── README.md

🔐 Security Feature

Each user can only access their own diary entries.
Data is protected using Django authentication system.

🎯 Future Improvements
Add password reset feature
Add diary search functionality
Add calendar view
Deploy on cloud (Heroku / Render)
Add REST API version

👨‍💻 Author

Vivek
Backend Developer | Django Enthusiast

⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

###################################################################################################
# 📝 Personal Diary App (Django)

A secure and simple web-based Personal Diary application built using Django.  
It allows users to write, manage, and store daily personal notes with authentication and privacy.

---

## 🚀 Features

- User Registration & Login System
- Secure Authentication (Login/Logout)
- Create personal diary entries
- Edit and update entries
- Delete entries
- View all past entries
- User-specific private data (each user sees only their diary)
- Clean and responsive UI using Bootstrap

---

## 🛠️ Tech Stack

- Python
- Django Framework
- SQLite Database
- HTML5
- CSS3
- Bootstrap

---

## 📸 Project Preview

*(Add screenshots here for better impression)*

Example:
- Login Page
- Dashboard
- Create Diary Entry Page

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
# 📝 Personal Diary App (Django)

A secure and simple web-based Personal Diary application built using Django.  
It allows users to write, manage, and store daily personal notes with authentication and privacy.

---

## 🚀 Features

- User Registration & Login System
- Secure Authentication (Login/Logout)
- Create personal diary entries
- Edit and update entries
- Delete entries
- View all past entries
- User-specific private data (each user sees only their diary)
- Clean and responsive UI using Bootstrap

---

## 🛠️ Tech Stack

- Python
- Django Framework
- SQLite Database
- HTML5
- CSS3
- Bootstrap

---

** 📸 Project Preview 
![Dashboard](static/images/dashboard.png)


Example:
- Login Page
- Dashboard
- Create Diary Entry Page

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/vivek8699-web/Django_project_dairy.git
cd personal-diary-app

```
## Create virtual environment
```bash
python -m venv venv

```
## Activate in window
```bash
venv\Scripts\activate.ps1
```
for linux/mac os
```bash
source venv/bin/activate

```
Install dependencies
```bash
pip install -r requirements.txt

```
Run migrations
```bash
python manage.py makemigrations
python manage.py migrate

```
Create superuser (optional)
```bash
python manage.py createsuperuser

```
Run server
```bash
python manage.py runserver


##############################################################################################







