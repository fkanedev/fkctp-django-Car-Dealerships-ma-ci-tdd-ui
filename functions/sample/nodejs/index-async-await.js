/**
 * Get all databases


const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
      const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
      const cloudant = CloudantV1.newInstance({
          authenticator: authenticator
      });
      cloudant.setServiceUrl(params.COUCH_URL);
      try {
        let dbList = await cloudant.getAllDbs();
        return { "dbs": dbList.result };
      } catch (error) {
          return { error: error.description };
      }
}
 */

/**************************************************************************************************/

/**
 * Get all dealerships
 */

/* const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
  const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
  const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
  });
  cloudant.setServiceUrl(params.COUCH_URL);
  try {
    let dbName = "dealerships"; 
    let recordsList = await getAllRecords(cloudant, dbName);
    return { "dealerships": recordsList.result };
  } catch (error) {
      return { error: error.description };
  }
} */


const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
  const authenticator = new IamAuthenticator({ apikey: params.IAM_API_KEY })
  const cloudant = CloudantV1.newInstance({
      authenticator: authenticator
  });
  cloudant.setServiceUrl(params.COUCH_URL);
  try {
    let dbName = "dealerships";
    let selector = {state: params.state};
    let recordsList = await getMatchingRecords(cloudant, dbName, selector);
    return { "dealerships": recordsList.result };
  } catch (error) {
      return { error: error.description };
  }
}


/*
Sample implementation to get all the records in a db.
*/
async function getAllRecords(cloudant,dbname) {

 try {
    let allRecords = await cloudant.postAllDocs({ db: dbname, includeDocs: true, limit: 10 });
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

