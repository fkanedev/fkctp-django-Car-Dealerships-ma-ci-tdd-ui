![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)
![Built with Django](https://img.shields.io/badge/Built%20with-Django-brightgreen.svg)
![Authentication - Django](https://img.shields.io/badge/Authentication-Django-blue.svg)
![Session Management - Django](https://img.shields.io/badge/Session%20Management-Django-orange.svg)
![Cloud Platforms - IBM Cloud](https://img.shields.io/badge/Cloud%20Platforms-IBM%20Cloud-blue.svg)
![CI/CD - GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

# Car Management Application
This project aims to develop a Django-based web application for comprehensive cars dealership management, vehicle reviews and personalized user experiences. It demonstrates the practical application of Django in a real-world scenario. It's part of my training in the [IBM Full Stack Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer) utilizing a [template](https://github.com/ibm-developer-skills-network/agfzb-CloudAppDevelopment_Capstone) provided by IBM Developer Skills Network.

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
   - Proxy Services
7. [CI/CD](#ci-cd)
8. [Deployment](#deployment)
9. [Sources](#sources)
10. [License](#license)
11. [Contact](#contact)

## 1. Introduction <a name="introduction"></a>

### Project Objective
The primary objective of this project is to develop a comprehensive car management system using the Django framework. The system is designed to facilitate dealership listings, customer reviews, dealer information, and user interactions through a user-friendly web interface, while ensuring robust user authentication and role-based access control.

### Key Features
- **Dealership Management** : Allows administrators to add, update, and manage dealership listings and details.
- **Vehicle Reviews** : Enables customers to add reviews and ratings for vehicles and dealerships.
- **Sentiment Analysis** : Utilizes natural language processing to analyze the tone and sentiment of user reviews.
- **Dealer Details** : Provides comprehensive information about each dealer, including contact details and location.
- **User Interaction** : Includes features for user registration, authentication, and personalized user experiences.

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
   
## 3. Technologies Used <a name="technologies-used"></a>

### Programming Languages
- **Python** : The core language used for backend development with Django.

### Tools and Frameworks
- **Django** : A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **SQLite** : A lightweight, disk-based database used for local development.

### Cloud Platforms
- **IBM Cloud** : Used for cloud functions (serverless computing), database management with Cloudant, and deployment using Cloud Foundry.
  
## 4. Installation and Configuration <a name="installation-and-configuration"></a>

### Prerequisites
Before setting up the project, 
- Ensure that you have the following installed on your local machine:
   - **Python 3.x** : The latest version of Python.
   - **Pip** : Python's package installer.
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
## 5. Usage <a name="usage"></a>
### Running the Server
To start the development server, navigate to the project directory and run:
   ```bash
   python manage.py runserver
   ```
This command will start the server at http://127.0.0.1:8000/.

### Accessing the Application
Once the server is running, open your web browser and go to http://127.0.0.1:8000/ to access the application. You will be able to register as a new user, log in, and explore the car management features.

## 6. Development <a name="development"></a>
### Project Structure 
- **server/djangobackend/** : The main Django project directory containing settings and configurations.
- **server/djangoapp/** : Contains the core application responsible for car and dealerships related functionalities.
- **server/static/** : Holds static files such as CSS and JavaScript.
- **cloudant/** : Contains the database configurations and scripts to create the necessary databases in the remote Cloudant repository.
- **functions/** : Contains the functions to be deployed on IBM Cloud Functions, including :
   - Node.js functions for retrieving dealership information
   - Python functions for retrieving and posting reviews.

### Templates
The project uses Django's templating system for rendering HTML. Templates are located in [server/djangoapp/templates/djangoapp](https://github.com/fkanedev/fkctp-django-Car-Dealerships-ma-ci-tdd-ui/tree/master/server/djangoapp/templates/djangoapp) include:
- **index.html** : Presents the dealerships (branches) list in a Bootstrap table, with attributes *(ID, Dealer Name, City, Address, Zip, State)* for each dealer.
- **navbar.html** : Displays the navigation bar.
- **registration.html** : Displays a "Sign Up" form for new users.
- **about.html** and **contact.html** : Refer to national company's (Cars Dealership) presentation.
- **dealer_details.html** : A detailed dealer page to show all reviews for the dealer. each review is displayed as a Bootstrap card, containing an (positve, neutral or negative) emoji according to the result of review's sentiment/tone analysis. A link to add reviews will be available for authenticated user.    
- **add_review.html** : A review submission page to allow user create a review for a dealer.
 
These templates leverage Django template tags and Bootstrap for styling and layout.

### Views
View functions in `server/djangoapp/views.py` handle HTTP requests and render appropriate templates. Key view functions include:

- **about** : Renders a static about page.
- **contact** : Renders a static contact page.
- **login_request** : Handles user login.
- **logout_request** : Handles user logout.
- **registration_request** : Handles user registration.
- **get_dealerships** : Renders the index page with a list of dealerships retrieved from IBM Cloud Functions.
- **get_dealer_details** : Renders the reviews of a specific dealer, including dealer information and reviews retrieved from IBM Cloud Functions.
- **add_review** : Handles the submission of a new review for a dealer.

These views utilize Django's powerful request handling and template rendering capabilities to dynamically generate content based on user interactions and database queries.

### Models
Django models in `server/djangoapp/models.py` define the structure of the database tables. Key models include:

- **CarMake**: Represents a car make with fields for name and description.
- **CarModel**: Represents a car model with a many-to-one relationship to CarMake. Fields include name, dealer ID, type, and year.
- **CarDealer**: A plain Python class to hold dealer data, including address, city, full name, latitude, longitude, short name, state, and zip.
- **DealerReview**: A plain Python class to hold review data, including car make, car model, car year, dealership, review ID, reviewer name, purchase status, purchase date, review text, and sentiment.

These models are defined using Django's ORM, providing a high-level abstraction for database operations, making it easy to create, retrieve, update, and delete records.

### Proxy Services
The file `server/djangoapp/restapis.py` contains functions that act as proxy services to interact with external APIs and services, facilitating data retrieval and analysis for the application. Key functions include:

- **get_request** : Makes HTTP GET requests to specified URLs, optionally using API key authentication.
- **post_request** : Makes HTTP POST requests to specified URLs with given JSON payloads.
- **get_dealers_from_cf** : Retrieves a list of car dealerships from a cloud function and parses the JSON response into a list of `CarDealer` objects.
- **get_dealer_by_id** : Retrieves a car dealership by its ID from a cloud function and parses the JSON response into a list of `CarDealer` objects.
- **get_dealer_by_state** : Retrieves car dealerships by state from a cloud function and parses the JSON response into a list of `CarDealer` objects.
- **get_dealer_reviews_from_cf** : Retrieves reviews for a specific dealership from a cloud function and parses the JSON response into a list of `DealerReview` objects.
- `analyze_review_sentiments` : Analyzes the sentiment of a review using IBM Watson Natural Language Understanding (NLU) and returns the sentiment label (e.g., Positive, Negative).

These proxy services enable seamless integration with external systems, providing essential data and insights for the application's functionality.

## 7. Continuous Integration and Continuous Delivery (CI/CD) <a name="ci-cd"></a>
The `.github/workflows/` directory contains GitHub Actions workflows that automate various Continuous Integration and Continuous Deployment (CI/CD) processes for the project. These workflows ensure code quality, facilitate automated testing, and manage deployments. Key workflows include:

- **linter.yml** : Automates code linting to ensure code quality and adherence to coding standards.
  - **Linting JavaScript Function** : Performs linting using npm.
  - **Linting Python Function** : Lints Python files, disabling certain checkers for line length, invalid names, and duplicate code.
  - **Linting Django Server** : Lints Django server Python files.

- **push-cf.yml**: Automates the build and deployment process to IBM Cloud Foundry.
  - **Setup, Build, Publish, and Deploy**:
    - Runs on `ubuntu-latest`.
    - Installs IBM CLI and Code Engine plugin.
    - Logs into IBM Cloud using an API key stored in secrets.
    - Creates a project in IBM Cloud Code Engine.
    - Lists all applications in the project.
    - Deploys the application using IBM Cloud Code Engine with buildpacks strategy.

These CI/CD workflows help maintain high code quality and streamline the deployment process, ensuring that new changes are tested and deployed efficiently.

## 8. Deployment <a name="deployment"></a>
To stay current with technological trends and ensure flexibility, containerizing the dealership application let us deploy it across multiple cloud providers. This approach enhances flexibility and prevents vendor lock-in, as all the big cloud providers have a way to host and manage containers. 

- **Containerization with Docker** :
  Use the below command to make [server/entrypoint.sh](https://github.com/fkanedev/fkctp-django-Car-Dealerships-ma-ci-tdd-ui/blob/master/server/entrypoint.sh) executable.

  ```bash
  chmod +x ./entrypoint.sh
  ```
  build your image and push to IBM Cloud Image Registry (ICR). Replace or export your ibmcloud namespace in *$MY_NAMESPACE*.

  ```bash
  docker build -t us.icr.io/$MY_NAMESPACE/dealership .
  ```

  ```bash
  docker push us.icr.io/$MY_NAMESPACE/dealership
  ```

- **Deployment with Kubernetes** :
   Kubernetes is an open-source container orchestration platform (used by cloud providers) that automates the deployment, management, and scaling of applications. [server/deployment.yaml](https://github.com/fkanedev/fkctp-django-Car-Dealerships-ma-ci-tdd-ui/blob/master/server/deployment.yaml) file is used to create the deployment and the service.

  Create the deployment using the following command and your deployment file. 

  ```bash
  kubectl apply -f deployment.yaml
  ```
     Add `*/djangoapp` at the end of the URL to see your application.
   
  Use port-forwarding (if needed) to see the running application. 

  ```bash
  kubectl port-forward deployment.apps/dealership 8000:8000
  ```

## 9. Sources <a name="sources"></a>

- **Template : [IBM Developer Skills Network - Cloud App Development Capstone template](https://github.com/ibm-developer-skills-network/agfzb-CloudAppDevelopment_Capstone)**

- **Useful links** :
  - **[Full Stack Application Development Capstone Project](https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone/home/week/1)**
  - **[IBM Full Stack Software Developer Professional Certificate](https://www.coursera.org/professional-certificates/ibm-full-stack-cloud-developer)**

## 10. License <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

## 11. Contact <a name="contact"></a>

### Contact Information :

- Send me email : **fkanecloudtech@gmail.com**
- Connect with me on [LinkedIn](https://www.linkedin.com/in/your-profile/)
- Visit my [portfolio](https://yourname.github.io) to explore my projects and services.

### Contribution and Support :

Contributions are welcome. Please refer to the [CONTRIBUTING](/CONTRIBUTING) file for more information on how to contribute.

