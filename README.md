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
2. [Architecture](#architecture)
3. [Technologies Used](#technologies-used)
4. [Installation and Configuration](#installation-and-configuration)
5. [Usage](#usage)
6. [Development](#development)
   - Project Structure
   - Templates
   - Views
   - Models
7. [CI/CD](#ci-cd)
8. [Deployment](#deployment)
9. [Sources](#sources)
10. [License](#license)
11. [Contact](#contact)

## 1. Introduction <a name="introduction"></a>

### Project Objective
The primary objective of this project is to develop a comprehensive car management system using the Django framework. The system is designed to facilitate dealership listings, customer reviews, dealer information, and user interactions through a user-friendly web interface, while ensuring robust user authentication and role-based access control.

### Key Features
- **Dealership Management**: Allows administrators to add, update, and manage dealership listings and details.
- **Vehicle Reviews**: Enables customers to add reviews and ratings for vehicles and dealerships.
- **Dealer Details**: Provides comprehensive information about each dealer, including contact details and location.
- **User Interaction**: Includes features for user registration, authentication, and personalized user experiences.

## 2. Architecture <a name="architecture"></a>
*Note: In this section, the architectural solution, diagram and design guidelines are provided by the training course. See the [Sources](#sources) section for more details.*
   - Key Components
      - **Django application** : The user interacts with the Django application through a web browser. 
      - **SQLite database** : The Django application handles the user authentication using the SQLite database as the persistance layer. The SQLite database also stores the Car Make and the Car Model data.
      - **Cloudant** : The dealerships and the reviews are stored in Cloudant, a NoSQL document based database.
      - **IBM Cloud functions** : Are used to interface with the Cloudant database to get dealerships, get reviews and post reviews.
      - **IBM Watson NLU service** : Watson NLU (Natural Language Understanding) service is used  to analyze sentiment/tone  review comments posted by users. 
      - **Proxy services** : The Django application talks to the IBM Cloud Functions and Watson NLU service via a set or proxy services.
 
   - Architectural Diagram
   
## 2. Technologies Used <a name="technologies-used"></a>

### Programming Languages
- **Python**: The core language used for backend development with Django.

### Tools and Frameworks
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite**: A lightweight, disk-based database used for local development.

### Cloud Platforms
- **IBM Cloud**: Used for cloud functions (serverless computing), database management with Cloudant, and deployment using Cloud Foundry.
  
## 3. Installation and Configuration <a name="installation-and-configuration"></a>

### Prerequisites
Before setting up the project, 
- Ensure that you have the following installed on your local machine:
   - **Python 3.x**: The latest version of Python.
   - **Pip**: Python's package installer.
- Sign up for IBM Cloud Lite account and create a Watson Natural Language Understanding service.

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
- cloudant/: Contains the database configurations and scripts to create the necessary databases in the remote Cloudant repository.
- functions/: Contains the functions to be deployed on IBM Cloud Functions, including :
   - Node.js functions for retrieving dealership information
   - Python functions for retrieving and posting reviews.

### Templates
The project uses Django's templating system for rendering HTML. Templates are located in [server/djangoapp/templates/djangoapp](https://github.com/fkanedev/fkctp-django-Car-Dealerships-ma-ci-tdd-ui/tree/master/server/djangoapp/templates/djangoapp) include:
- **index.html** : Presents the dealerships list in a Bootstrap table, with attributes (ID, Dealer Name, City, Address, Zip, State) for each dealer.
- **about.html** and **contact.html** : Refer to company's (Cars Dealership) presentation.
- **add_review.html** : 
- **dealer_details.html** : 
- **registration.html** : 
- **navbar.html** :

These templates leverage Django template tags and Bootstrap for styling and layout.

### Views
View functions in onlinecourse/views.py handle HTTP requests and render appropriate templates. Key view functions include:


These views utilize Django's powerful request handling and template rendering capabilities to dynamically generate content based on user interactions and database queries.

### Models
Django models in onlinecourse/models.py define the structure of the database tables. Key models include:

The models are defined using Django's ORM, which provides a high-level abstraction for database operations, making it easy to create, retrieve, update, and delete records.


## 6. Sources <a name="sources"></a>

- **Template: [IBM Developer Skills Network - Cloud App Development Capstone template](https://github.com/ibm-developer-skills-network/agfzb-CloudAppDevelopment_Capstone)**

- **Useful links**:
  - **[Full Stack Application Development Capstone Project](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/home/week/1)**
  - **[IBM Full Stack Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer)**

## 7. License <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

## 8. Contact <a name="contact"></a>

### Contact Information :

- Send me email : **fkanecloudtech@gmail.com**
- Connect with me on [LinkedIn](https://www.linkedin.com/in/your-profile/)
- Visit my [portfolio](https://yourname.github.io) to explore my projects and services.

### Contribution and Support :

Contributions are welcome. Please refer to the [CONTRIBUTING](/CONTRIBUTING) file for more information on how to contribute.

