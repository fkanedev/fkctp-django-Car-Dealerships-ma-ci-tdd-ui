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
#from ibmcloudant.cloudant_v1 import CloudantV1, Document
#import requests
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

    db_name = "reviews"
    code = 200
    message = "Request success."
    record = {}
    result = {}

    try:
        
        authenticator = IAMAuthenticator(IAM_API_KEY)
        service = CloudantV1(authenticator=authenticator)
        service.set_service_url(CLOUDANT_URL)
        param_dealer_id = 0
        if param_dict:
            param_dealer_id = int(param_dict['dealerId'])

    except ApiException as error:
        code = 500
        message = "unable to connect!"
        result = { "error": error.message }

    if param_dealer_id:
        try:
            selector = {'dealership': {'$eq': param_dealer_id}}
            record = service.post_find(db=db_name, selector=selector).get_result()
            result = {"reviews": record["docs"]}
            if len(result) == 0:
                code = 404
                message = f"The dealership with id key {param_dealer_id} does not exist."
        except ApiException as error:
            code = 500
            message = "Something went wrong on the server."
            result = { "error": error.message }
    else:
        try:
            record = service.post_all_docs(db=db_name, include_docs=True).get_result()
            result = {"reviews": record["rows"]}
            if len(result) == 0:
                code = 404
                message = "The reviews database is empty."
        except ApiException as error:
            code = 500
            message = "Something went wrong on the server."
            result = { "error": error.message }

    response = {
        "statusCode": code,
        "message" : message,
        "headers": { 'Content-Type': 'application/json' },
        "body": result
    }

    return response



