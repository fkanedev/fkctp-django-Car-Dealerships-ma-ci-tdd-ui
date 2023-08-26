#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#

"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from ibm_cloud_sdk_core import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibmcloudant.cloudant_v1 import CloudantV1, Document
import requests
#from requests import ConnectionError, ReadTimeout, RequestException, ValueError
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

IAM_API_KEY = "nM2froRZmoB_NIbhHyFNaqZIecGlT8PTxbh5henG5UYS"
CLOUDANT_URL = "https://e844e385-41bd-4c23-981f-f0dc16b466aa-bluemix.cloudantnosqldb.appdomain.cloud"


def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """
    
    DB_NAME = "reviews";
    code = 200
    message = "Request success."
    record = {}
    result = {}
    
    try:
        
        authenticator = IAMAuthenticator(IAM_API_KEY)
        service = CloudantV1(authenticator=authenticator)
        service.set_service_url(CLOUDANT_URL)
        PARAM_REVIEW = {}
        if param_dict:
            PARAM_REVIEW = param_dict['review']
        
    except ApiException as ae:
        code = 500
        message = "unable to connect."
        result = { "error": ae.message }

    
    if PARAM_REVIEW:
        try:
            record = service.post_document(db=DB_NAME, document=PARAM_REVIEW).get_result()
            result = record
            if len(result) == 0:
                code = 404
                message = f"The dealership with id key {PARAM_DEALER_ID} does not exist."
        except ApiException as ae:
            code = 500
            message = "Something went wrong on the server."
            result = { "error": ae.message }
    else:
        code = 400
        message = "The request body is empty. No review added."
  
    response = {
        "statusCode": code,
        "message" : message,
        "headers": { 'Content-Type': 'application/json' },
        "body": result
    }
    
    return response


