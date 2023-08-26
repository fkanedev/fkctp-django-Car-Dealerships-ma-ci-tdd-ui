import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
from ibm_watson.natural_language_understanding_v1 \
    import Features, SentimentOptions
import asyncio


# WATSON NLU analyzer parameters
WATSON_URL = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/6d92a0fc-2ee3-4aa4-bcdd-21f611eb9e02"
WATSON_API_KEY = "PxYfd9NcYJLT-fp3tDgcX3-tk1TQNAWEflZa_jtQTeRw"


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
async def get_request(url, has_apikey=False, **kwargs):
    
    json_data = {}
    try:
        # Call get method of requests library with URL and parameters        
        if has_apikey:

            api_key = kwargs['apikey']
            params = dict()
            params["text"] = kwargs["text"]
            params["version"] = kwargs["version"]
            params["features"] = kwargs["features"]
            params["return_analyzed_text"] = kwargs["return_analyzed_text"]
            # Basic authentication GET
            response = await requests.get(url, headers={'Content-Type':'application/json'}, 
                                auth=HTTPBasicAuth('apikey', api_key), params=params)
            json_data = json.loads(response.text)
        else:
            
            response = requests.get(url, headers={'Content-Type':'application/json'}, params=kwargs)
            json_data = json.loads(response.text)
    except:
        # If any error occurs
        print("Network exception occurred.")
    #status_code = response.status_code
    #print("With status {}".format(status_code))
    
    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)
def post_request(url, json_payload, **kwargs):

    #json_data = {}
    try:
        # Call get method of requests library with URL and parameters
        response = requests.post(url, headers={'Content-Type':'application/json'}, params=kwargs,
                                    json=json_payload)
        #json_data = json.loads(response.text)
    except:
        # If any error occurs
        print("Network exception occurred")
    #status_code = response.status_code
    #print("With status {}".format(status_code))
    
    return response


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
async def get_dealers_from_cf(url, **kwargs):

    results = []
    # Call get_request with a URL parameter
    json_result = await get_request(url, **kwargs)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result['dealerships']
        # For each dealer object
        for dealer in dealers:
            # Get its content in 'doc' object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in 'doc' object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], 
                                   full_name=dealer_doc["full_name"], id=dealer_doc["id"], 
                                   lat=dealer_doc["lat"], long=dealer_doc["long"], 
                                   short_name=dealer_doc["short_name"], 
                                   st=dealer_doc["st"], state=dealer_doc["state"], 
                                   zip=dealer_doc["zip"])
            results.append(dealer_obj)
        return results


# Create a get_dealer_by_id method to get dealers by dealer id from a cloud function
# def get_dealer_by_id(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
async def get_dealer_by_id(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = await get_request(url, dealerId=dealerId)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["dealerships"]
        # For each dealer object
        for dealer_doc in dealers:
            # Get its content in 'doc' object
            #dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in 'doc' object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], 
                                   full_name=dealer_doc["full_name"], id=dealer_doc["id"], 
                                   lat=dealer_doc["lat"], long=dealer_doc["long"], 
                                   short_name=dealer_doc["short_name"], 
                                   st=dealer_doc["st"], state=dealer_doc["state"], 
                                   zip=dealer_doc["zip"])
            results.append(dealer_obj)
        return results


# Create a get_dealer_by_state method to get dealers by state from a cloud function
# def get_dealer_by_state(url, state):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
async def get_dealer_by_state(url, state):
    results = []
    # Call get_request with a URL parameter
    json_result = await get_request(url, state=state)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in 'doc' object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in 'doc' object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], 
                                   full_name=dealer_doc["full_name"], id=dealer_doc["id"], 
                                   lat=dealer_doc["lat"], long=dealer_doc["long"], 
                                   short_name=dealer_doc["short_name"], 
                                   st=dealer_doc["st"], state=dealer_doc["state"], 
                                   zip=dealer_doc["zip"])
            results.append(dealer_obj)
        return results


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_reviews_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerReview object list
async def get_dealer_reviews_from_cf(url, dealerId):
    results = []
    # Call get_request with a URL parameter
    json_result = await get_request(url, dealerId=dealerId)
    if json_result:
        # Get the row list in JSON as reviews
        reviews = json_result["reviews"]
        # Each review is already a doc object
        for review_doc in reviews:
            # Create a DealerReview object with values in 'doc' object
            params = {"car_make":"", "car_model":"", "car_year":"", "dealership":"", 
                      "id":"", "name":"", "purchase":"", "purchase_date":"", "review":"", 
                      "sentiment":""}
            for k in params.keys():
                # To avoid key error, let's check if it exist
                if k in review_doc.keys():
                    params[k] = review_doc[k]
            
            sentiment_label = await analyze_review_sentiments(review_doc["review"])
            params["sentiment"] = sentiment_label

            review_obj = DealerReview(**params)
            results.append(review_obj)
        return results

# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative
async def analyze_review_sentiments(text):
    url = WATSON_URL + "/v1/analyze"
    params = dict()
    params["apikey"] = WATSON_API_KEY
    params["text"] = text
    params["version"] = "2022-04-07"
    # Features(sentiment=SentimentOptions(document=True))
    params["features"] = "sentiment" 
    params["sentiment.document"] = "true"
    params["return_analyzed_text"] = True
    
    result = await get_request(url=url, has_apikey=True, **params)
    label = result["sentiment"]["document"]["label"]

    return label


