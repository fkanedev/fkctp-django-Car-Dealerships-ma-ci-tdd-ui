/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */
  
  
 /**
 * Get all databases
 * Results:
 * {
 *  "dbs": [
 *      "dealerships",
 *      "reviews"
 *  ]
 * }
 * 
 * /

/**
 * Get all dealerships
 */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

const IAM_API_KEY = "nM2froRZmoB_NIbhHyFNaqZIecGlT8PTxbh5henG5UYS";
const CLOUDANT_URL = "https://e844e385-41bd-4c23-981f-f0dc16b466aa-bluemix.cloudantnosqldb.appdomain.cloud";

async function main(params) {

  const authenticator = new IamAuthenticator({ apikey: IAM_API_KEY })
  const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
  });
  cloudant.setServiceUrl(CLOUDANT_URL);

  const dbName = "dealerships";
  let code = 200
  let message = "Request success."
  let recordsList = {}
  let result = {}

  if (params.dealerId){
        
        try {           
          let selector = {id: params.dealerId};
          let recordsList = await getMatchingRecords(cloudant, dbName, selector);
          result = { "dealerships": recordsList.result };
          if (recordsList.result.length == 0){
            code = 404
            message = "The dealership with id key {param.dealerId} does not exist"
          }
        } catch (error) {
            code = 500
            message = "Something went wrong on the server."
            result = { error: error.description };
        }

  } else if (params.state){
    
          try {           
            let selector = {state: params.state};
            let recordsList = await getMatchingRecords(cloudant, dbName, selector);
            result = { "dealerships": recordsList.result };
            if (recordsList.result.length == 0){
                code = 404
                message = "The dealership with state key ${param.state} does not exist"
            }
          } catch (error) {
              code = 500
              message = "Something went wrong on the server."
              result = { error: error.description };
          }

  } else {
  
        try { 
          let recordsList = await getAllRecords(cloudant, dbName);
          result = { "dealerships": recordsList.result };
          if (recordsList.result.length == 0){
            code = 404
            message = "The dealerships database is empty."
          }
        } catch (error) {
            code = 500
            message = "Something went wrong on the server."
            result = { error: error.description };
        }
  }

  let response = {
    statusCode: code,
    message : message,
    headers: { 'Content-Type': 'application/json' },
    body: result    
  }

  return response
}

/*
Sample implementation to get all the records in a db.
*/
async function getAllRecords(cloudant,dbname) {

 try {
    let allRecords = await cloudant.postAllDocs({ db: dbname, includeDocs: true});
    return {result: allRecords.result.rows};
  } catch (error) {
      return { error: error.description };
  }

}

/*
 Sample implementation to get the records in a db based on a selector. If selector is empty, it returns all records. 
 eg: selector = {state:"Texas"} - Will return all records which has value 'Texas' in the column 'State'
 */
 async function getMatchingRecords(cloudant,dbname, selector) {

  try {
    let matchingRecords = await cloudant.postFind({db:dbname,selector:selector});
    return {result: matchingRecords.result.docs};
  } catch (error) {
      return { error: error.description };
  }
}