"""IBM Cloud Function that gets all reviews for a dealership

Returns:
    List: List of reviews for the given dealership
"""
from ibmcloudant.client import Cloudant
from ibmcloudant.error import CloudantException
import requests


def main(param_dict, request):
    """Main Function

    Args:
        param_dict (Dict): input paramater

    Returns:
        _type_: _description_ TODO
    """

    try:
        client = Cloudant.iam(
            account_name=param_dict["COUCH_USERNAME"],
            api_key=param_dict["IAM_API_KEY"],
            connect=True,
        )
        #print(f"Databases: {client.all_dbs()}")
        reviews_db = client['reviews']
        user_review = request.POST['user_review']
        review_exist = user_review['id'] in reviews_db
        message = ""
        if review_exist:
            selector = {'id': {'$eq': user_review['id']}}
            doc = reviews_db.get_query_result(selector)
            doc['review'] = user_review['review']
            message = "User's review updated."

        else:
            doc = reviews_db.create_document(user_review)
            message = "User's review created."

    except CloudantException as cloudant_exception:
        print("unable to connect")
        return {"error": cloudant_exception}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        return {"error": err}

    return {
            "body": message
            }

