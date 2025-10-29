# Django HTML Forms (POST Method Example)

This project demonstrates how to build a simple **HTML form** in Django using the **POST** method and retrieve form data using `request.POST`.  
It includes a username and password input form, displays the submitted values, and shows how to handle POST requests in Django views.

---

##  Features
- Simple HTML form using POST  
- CSRF protection (`{% csrf_token %}`)  
- Handling form submission in Django views  
- Returning dynamic output using `HttpResponse`  
- Beginner-friendly project structure  

---

##  Tech Stack
- Python 3.x  
- Django 4.x / 5.x  
- HTML5  

---

##  Project Structure
project_root/
│── templates/
│ └── htmlforms.html
│── myapp/
│ ├── views.py
│── project_root/
│ ├── settings.py
│ ├── urls.py
│── manage.py
