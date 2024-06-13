![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)
![Built with Django](https://img.shields.io/badge/Built%20with-Django-brightgreen.svg)
![Authentication - Django](https://img.shields.io/badge/Authentication-Django-blue.svg)
![Session Management - Django](https://img.shields.io/badge/Session%20Management-Django-orange.svg)
![Cloud Platforms - IBM Cloud](https://img.shields.io/badge/Cloud%20Platforms-IBM%20Cloud-blue.svg)
![CI/CD - GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

# Car Management Application
This project involves developing a web application using Django for managing car information, vehicle authentication, user roles, and a service feature for booking cars. It demonstrates the practical application of Django in a real-world scenario. It's part of my training in the [IBM Full Stack Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer) utilizing a [template](https://github.com/ibm-developer-skills-network/final-cloud-app-with-database) provided by IBM Developer Skills Network.

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Installation and Configuration](#installation-and-configuration)
4. [Usage](#usage)
5. [Development](#development)
   - Project Structure
   - Templates
   - Views
   - Models
6. [CI/CD](#ci-cd)
7. [Deployment](#deployment)
8. [Sources](#sources)
9. [License](#license)
10. [Contact](#contact)

## 1. Introduction <a name="introduction"></a>

### Project Objective
The primary objective of this project is to develop a comprehensive car management system using the Django framework. The system is designed to facilitate dealership listings, customer reviews, dealer information, and user interactions through a user-friendly web interface, while ensuring robust user authentication and role-based access control.

### Key Features
- **Dealership Management**: Allows administrators to add, update, and manage dealership listings and details.
- **Vehicle Reviews**: Enables customers to add reviews and ratings for vehicles and dealerships.
- **Dealer Details**: Provides comprehensive information about each dealer, including contact details and location.
- **User Interaction**: Includes features for user registration, authentication, and personalized user experiences.

## 2. Technologies Used <a name="technologies-used"></a>

### Programming Languages
- **Python**: The core language used for backend development with Django.

### Tools and Frameworks
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite**: A lightweight, disk-based database used for local development.

### Cloud Platforms
- **IBM Cloud**: Used for hosting the application, database management with Cloudant, and deployment using Cloud Foundry.
  
## 3. Installation and Configuration <a name="installation-and-configuration"></a>

### Prerequisites
Before setting up the project, ensure that you have the following installed on your local machine:
- **Python 3.x**: The latest version of Python.
- **Pip**: Python's package installer.

### Installation Steps
1. **Clone the repository**:
   ```sh
   git clone https://github.com/fkanedev/fkctp-tmp-car
   cd fkctp-tmp-car
   ```
2. Install the dependencies:
  ```bash
   pip install -r requirements.txt
   ```
### Environment Setup
- Use manage.py for server management operations.
## 4. Usage <a name="usage"></a>
### Running the Server
To start the development server, navigate to the project directory and run:
   ```bash
   python manage.py runserver
   ```
This command will start the server at http://127.0.0.1:8000/.

### Accessing the Application
Once the server is running, open your web browser and go to http://127.0.0.1:8000/ to access the application. You will be able to register as a new user, log in, and explore the car management features.

## 5. Development <a name="development"></a>
### Project Structure 
- server/djangobackend/: The main Django project directory containing settings and configurations.
- server/djangoapp/: Contains the core application responsible for car and dealerships related functionalities.
- server/static/: Holds static files such as CSS and JavaScript.

### Templates
The project uses Django's templating system for rendering HTML. The main templates include:


These templates are located in onlinecourse/templates/onlinecourse/ and leverage Django template tags and Bootstrap for styling and layout.

### Views
View functions in onlinecourse/views.py handle HTTP requests and render appropriate templates. Key view functions include:


These views utilize Django's powerful request handling and template rendering capabilities to dynamically generate content based on user interactions and database queries.

### Models
Django models in onlinecourse/models.py define the structure of the database tables. Key models include:

The models are defined using Django's ORM, which provides a high-level abstraction for database operations, making it easy to create, retrieve, update, and delete records.

