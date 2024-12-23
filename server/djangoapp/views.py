from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import CarModel
from .restapis import get_dealers_from_cf, get_dealer_reviews_from_cf, post_request, get_dealer_by_id
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)
# ...


# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, "djangoapp/contact.html", context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)
# ...

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    
    logout(request)
    return redirect('djangoapp:index')
# ...

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}

    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)
    
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        password = request.POST['psw']

        user_exist = False
        try:    
            User.objects.get(username=username)
            user_exist = True        
        
        except ObjectDoesNotExist:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        
        if not user_exist:        
            user = User.objects.create_user(username=username, first_name=first_name, 
                                            last_name=last_name, password=password)
            login(request, user)

            return redirect('djangoapp:index')
        
        else:
            context['message'] = "User already exists!"
            return render(request, 'djangoapp/registration.html', context)
    
# ...


# Backends API endpoints and apikey
# API_KEY = ""
# get-dealerships
GET_DEALERS_URL = "https://eu-gb.functions.appdomain.cloud/api/v1/web/55d8a43f-069a-4474-b42c-d98d5acbd7ba/dealership-package/get-dealership"
# get-reviews
GET_REVIEWS_URL = "https://eu-gb.functions.appdomain.cloud/api/v1/web/55d8a43f-069a-4474-b42c-d98d5acbd7ba/dealership-package/get-reviews"
# post-review
POST_REVIEW_URL = "https://eu-gb.functions.appdomain.cloud/api/v1/web/55d8a43f-069a-4474-b42c-d98d5acbd7ba/dealership-package/post-review"


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    
    if request.method == "GET":
        # Get dealers from Cloud Functions
        dealerships = get_dealers_from_cf(GET_DEALERS_URL)
        context['dealerships_list'] = dealerships

        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    context = {}
    has_review = False
    dealer_name = ""

    if request.method == "GET":
        # Get dealership
        response = get_dealer_by_id(GET_DEALERS_URL, dealerId=dealer_id) 
        if len(response) != 0:
            dealer_obj = response[0]
            dealer_name = dealer_obj.full_name
        # Get reviews for the dealership with this dealer_id
        reviews = get_dealer_reviews_from_cf(GET_REVIEWS_URL, dealerId=dealer_id)
        if len(reviews) != 0:
            has_review = True
        context['dealer_id'] = dealer_id
        context['dealer_name'] = dealer_name
        context['has_review'] = has_review     
        context['reviews_list'] = reviews
        context['show_add_review_link'] = True

    return render(request, 'djangoapp/dealer_details.html', context)


# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    context = {}

    if request.method == "GET":
        # Get cars for this dealership
        cars_dealer_list = CarModel.objects.filter(dealer_id=dealer_id)
        context['dealer_id'] = dealer_id
        context['cars'] = cars_dealer_list
        #print(f"cars_dealer_list: {cars_dealer_list}")

        return render(request, 'djangoapp/add_review.html', context)

    if request.method == "POST":
        # Get username and password from request.POST dictionary
        review_content = request.POST['content']
        has_purchased_car = request.POST['purchasecheck']
        purchased_car_id = request.POST['car']
        purchase_date = request.POST['purchasedate']
        
        car = get_object_or_404(CarModel, pk=purchased_car_id)
        
        if request.user.is_authenticated:
            
            review = {
                "name": request.user.username,
                "dealership": dealer_id,
                "review": review_content,
                "purchase": has_purchased_car,
                "purchase_date": purchase_date,
                "car_make": car.make.make_name,
                "car_model": car.model_name,
                "car_year": car.year               
            }
            
            json_payload = {
                "review": review
            }

            response = post_request(url=POST_REVIEW_URL, json_payload=json_payload, dealerId=dealer_id)
            
            if response.status_code == 200:
                success_add_review = True 
                context['success_add_review'] = success_add_review
            
            return HttpResponseRedirect(reverse(viewname='djangoapp:dealer_details', args=(dealer_id,)))
    
    return render(request, 'djangoapp/add_review.html', context)
