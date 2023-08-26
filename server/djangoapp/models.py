from django.utils.timezone import now
from django.db import models
import datetime
#from django.conf import settings
#import sys
#import uuid
#try:
#    from django.db import models
#except Exception:
#    print("There was an error loading django modules. Do you have django installed?")
#    sys.exit()


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    make_name = models.CharField(null=False, max_length=30, default='car make')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"Car Make: {self.make_name}, Description: {self.description}"

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model_name = models.CharField(null=False, max_length=50, default='car model')
    dealer_id = models.IntegerField(default=0)
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon')
    ]
    type = models.CharField(
        null=False,
        max_length=30,
        choices=TYPE_CHOICES,
        default=SUV
    )
    YEAR_CHOICES = [(y, y) for y in range(1980, (datetime.datetime.now().year+1)) ]

    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    #year = models.DateField(default=now)

    def __str__(self):
        return f"Car Model: {self.model_name}, Type: {self.type}, Year: {self.year}."

# <HINT> Create a plain Python class `CarDealer` to hold dealer data

class CarDealer(models.Model):
    
    def __init__(self, address, city, full_name, lat, id, long, short_name, st, state,  zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer full_name
        self.full_name = full_name
        # Dealer lat
        self.lat = lat
        # Dealer id
        self.id = id
        # Dealer long
        self.long = long
        # Dealer short_name
        self.short_name = short_name
        # Dealer st (shortname state)
        self.st = st
        # Dealer state
        self.state = state
        # Dealer zip
        self.zip = zip

    def __str__(self) -> str:
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data

class DealerReview(models.Model):
    
    def __init__(self, car_make, car_model, car_year, dealership, id, name, purchase, purchase_date, review, sentiment):
        # Review car_make
        self.car_make = car_make
        # Review car_model
        self.car_model = car_model
        # Review car_year
        self.car_year = car_year
        # Review dealership
        self.dealership = dealership
        # Review id
        self.id = id
        # Review name
        self.name = name
        # Review purchase
        self.purchase = purchase
        # Review purchase_date
        self.purchase_date = purchase_date
        # Review review
        self.review = review
        # Review sentiment
        self.sentiment = sentiment

    def __str__(self) -> str:
        return "Review: " + self.review + "- by " + self.name