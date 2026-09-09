# 🎯 Point Blank

> **A Django-powered web platform for discovering and presenting firearms, ammunition, and tactical accessories through a structured, modern e-commerce experience.**

[![Django](https://img.shields.io/badge/Django-5.x-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## 🌐 Overview

**Point Blank** is a Django-based web application built around a modern firearm catalog and shopping workflow. The repository contains a dedicated `firearms` Django app, a `point_blank` project, reusable templates, static assets, product media, contact pages, authentication pages, cart and payment pages, and a SQLite database. 

The home page is designed around a strong hero section, featured products, trust indicators, and navigation to the product catalog. The current template also includes an age-verification gate and messaging around legal compliance.

---

## ✨ Features

### 🏠 Landing Page
- Hero section with strong visual branding
- Featured product section
- Product cards with pricing and caliber information
- Navigation to the catalog and information pages
- Age-verification interface
- Trust indicators and compliance messaging

### 🔫 Product Catalog
- Dedicated Arsenal/catalog page
- Product listing cards
- Firearm names, caliber, and pricing
- Individual product detail pages
- Product media stored in the repository

### 📋 Product Details
The product model stores fields for:
- Name
- Image
- Price
- Description
- Ammunition
- Ammunition capacity
- Caliber
- Barrel length
- Overall length
- Weight
- Finish
- Action
- Added date 

### 🛒 Shopping Workflow
The project includes dedicated templates for:
- Cart
- Payment
- Success
- Failure
- Login
- Registration
- Profile

### 📞 Additional Pages
The template collection also includes:
- About
- Contact
- 404 page
- Authentication pages
- Product detail page

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Backend programming |
| **Django** | Web framework, routing, views, models, templates |
| **SQLite** | Development database |
| **HTML5** | Page structure |
| **CSS3** | Custom interface styling |
| **JavaScript** | Client-side interactions |
| **Django Templates** | Dynamic page rendering |

The repository is structured as a Django project with `manage.py`, `requirements.txt`, the `point_blank` project, and a dedicated `firearms` application. 

---

## 📁 Project Structure

```text
Point-Blank/
│
├── contact/
├── firearms/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/
│   └── guns/
│
├── point_blank/
│   ├── asgi.py
│   └── ...
│
├── static/
│
├── templates/
│   ├── includes/
│   ├── about.html
│   ├── arsenal.html
│   ├── cart.html
│   ├── contact.html
│   ├── firearm-details.html
│   ├── index.html
│   ├── login.html
│   ├── payment.html
│   ├── profile.html
│   ├── register.html
│   ├── success.html
│   └── failure.html
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```

The current repository contains the Django app, templates, media, static assets, SQLite database, `manage.py`, and dependency file shown above.

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/WINSTER000/Point-Blank.git
cd Point-Blank
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scriptsctivate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🗄️ Database

The project currently includes a SQLite database:

```text
db.sqlite3
```

The `Firearms` model contains structured product information including pricing, descriptions, ammunition details, caliber, dimensions, weight, finish, action, and creation date.

For production use, database configuration should be reviewed and a production-grade database should generally be considered instead of committing a development SQLite database.

---

## 🔐 Responsible Use & Legal Compliance

This project is presented as a **web-development / e-commerce demonstration**.

Any real-world sale, purchase, transfer, shipping, or possession of regulated products must comply with all applicable laws and regulations in the relevant jurisdiction.

The website template itself includes age-verification and legal-compliance messaging.

This repository documentation does not provide instructions for acquiring, modifying, manufacturing, or using weapons.

---

## 🎯 Project Objectives

Point Blank demonstrates how Django can be used to build a complete catalog-oriented web application with:

- Server-side rendering
- Database-backed products
- Dynamic templates
- Product detail pages
- Authentication pages
- Shopping-cart flow
- Payment-page workflow
- Media management
- Static assets
- Responsive web design
- Form and session-based interactions

---

## 🚀 Future Improvements

Possible improvements include:

- Production database integration
- Secure payment gateway integration
- Improved authentication and authorization
- Product search and filtering
- Product categories
- Inventory management
- Order management
- Admin analytics
- Improved accessibility
- Automated tests
- Production deployment configuration
- Better media optimization
- Security hardening

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feature/your-feature
```

3. Make your changes.
4. Test the application.
5. Commit your changes:

```bash
git add .
git commit -m "Add: your feature"
```

6. Push your branch:

```bash
git push origin feature/your-feature
```

7. Open a Pull Request.

---

## 👨‍💻 Author

**WINSTER000**

GitHub:  
https://github.com/WINSTER000

Repository:  
https://github.com/WINSTER000/Point-Blank

---

<p align="center">

### 🎯 POINT BLANK

**Precision. Power. Protection.**

Built as a Django web-development project.

</p>
