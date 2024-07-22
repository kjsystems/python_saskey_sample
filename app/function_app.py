import azure.functions as func
import datetime
import json
import logging
from azure.storage.blob import BlobServiceClient

app = func.FunctionApp()

@app.route(route="add_saskey", auth_level=func.AuthLevel.FUNCTION)
def add_saskey(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    account_url = "https://<storage-account-name>.blob.core.windows.net"
    account_key = "<account-key>"
    blob_service_client = BlobServiceClient(account_url, credential=account_key)

    use_account_sas(blob_service_client=blob_service_client)

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

def use_account_sas(self, blob_service_client: BlobServiceClient):
    account_name = blob_service_client.account_name
    account_key = blob_service_client.credential.account_key
    sas_token = self.create_account_sas(account_name=account_name, account_key=account_key)

    account_sas_url = f"{blob_service_client.url}?{sas_token}"
    logging.info(f"Account SAS URL: {account_sas_url}")

    blob_service_client_sas = BlobServiceClient(account_url=account_sas_url)
