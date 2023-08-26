/**
 * Get dealerships by state
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
  const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
  const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
  });
  cloudant.setServiceUrl(params.COUCH_URL);
  const dbName = "dealerships";
  const search_params = {
                          id: params.dealerId, 
                          state: params.state
                        };
  let code = 200
  let message = "Request success."
  let recordsList = {}
  let result = {}
  
  search_params.forEach(async (k, v) => {
    if (v){

        try {           
          let selector = {k: v};
          let recordsList = await getMatchingRecords(cloudant, dbName, selector);
          result = { "dealerships": recordsList.result };
        } catch (error) {
          if (recordsList.result.docs.lenght == 0){
            code = 404
            message = "The dealership with state key 'texas' does not exist"
          } else {
            code = 500
            message = "Something went wrong on the server."
          }
          
          result = { error: error.description };
        }
    }
  })

  let response = {
    statusCode: code,
    message : message,
    headers: { 'Content-Type': 'application/json' },
    body: result    
  }

  return response
 
}


 