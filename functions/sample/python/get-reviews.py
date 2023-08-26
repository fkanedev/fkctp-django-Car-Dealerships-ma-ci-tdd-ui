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
from ibmcloudant.cloudant_v1 import CloudantV1, Document
import requests
#from requests import ConnectionError, ReadTimeout, RequestException, ValueError
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

IAM_API_KEY = "nM2froRZmoB_NIbhHyFNaqZIecGlT8PTxbh5henG5UYS"
CLOUDANT_URL = "https://e844e385-41bd-4c23-981f-f0dc16b466aa-bluemix.cloudantnosqldb.appdomain.cloud"


def main(param_dict):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """
    
    try:
        #client = CloudantV1.iam(
        #    account_name=param_dict["COUCH_USERNAME"],
        #    api_key=param_dict["IAM_API_KEY"],
        #    connect=True,
        #)
        #print(f"Databases: {client.all_dbs()}")
        
        authenticator = IAMAuthenticator(IAM_API_KEY)
        service = CloudantV1(authenticator=authenticator)
        service.set_service_url(CLOUDANT_URL)
        
        reviews_db = service['reviews'].get_result()
        selector = {'dealership': {'$eq': param_dict["dealerId"]}}
        docs = reviews_db.get_query_result(selector)

    except ApiException as ae:
        #print("unable to connect")
        return {
            "message": "unable to connect",
            "error": ae.message}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        #print("connection error")
        return {
            "message": "connection error",
            "error": err}

    return {"docs": docs}
