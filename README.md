# **Resume Forge**

---

## **💡 About the Project**

**Resume Forge** is a **Django-based resume generator web application** that allows users to:

- Fill out their personal, educational, and project details via forms  
- Dynamically generate a **professional resume** using predefined HTML templates and CSS styling  
- Download or print their generated resume

---

## **🔷 Key Features**

- Django forms for structured data collection  
- Dynamic rendering of data into templates  
- Clean and professional CSS styling  
- Modular project structure for easy updates

---

## **🗂️ Project Structure**

![Screenshot 2025-06-28 193304](https://github.com/user-attachments/assets/60ee25f5-6bad-4235-a33d-e91e730941c0)

---

## **⚙️ Execution Steps (Folder-wise)**

### ✅ **1. Open your terminal or command prompt**

Navigate to your project directory:

cd path/to/ResumeForge


 **2. Create virtual environment**
If not already created:
    **python -m venv venv**


 **3. Activate virtual environment**
For Windows:
venv\Scripts\activate

**4. Install required packages**
If requirements.txt is present:
     **pip install -r requirements.txt**
Otherwise, install Django manually:
     pip install django

**5. Apply database migrations**

python manage.py makemigrations
python manage.py migrate

**6. Run the Django development server**

python manage.py runserver

**7. Open the application in your browser**
Visit:
http://127.0.0.1:8000/
Fill out the form on index.html

Submit to generate your professional resume

![resume project](https://github.com/user-attachments/assets/3c16829c-e190-4f2c-8b7b-c03dbbf25f1b)
