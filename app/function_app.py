import azure.functions as func
import logging
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
import datetime

app = func.FunctionApp()

@app.route(route="add_saskey", auth_level=func.AuthLevel.FUNCTION)
def add_saskey(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')

    # 使用例
    account_name = "<your-account-name>"
    account_key = "<your-account-key>"
    container_name = "sample"
    blob_name = "sample.docx"

    sas_samples = SASSamples()
    blob_url = sas_samples.create_url_with_saskey(account_name, account_key, container_name, blob_name)

    return func.HttpResponse(f"blob_url: {blob_url}")

class SASSamples(object):

    def create_blob_sas(self, account_name: str, account_key: str, container_name: str, blob_name: str):
        # Create a SAS token that's valid for one day
        start_time = datetime.datetime.utcnow()
        expiry_time = start_time + datetime.timedelta(days=1)

        # Define the SAS token permissions
        sas_permissions = BlobSasPermissions(read=True)

        sas_token = generate_blob_sas(
            account_name=account_name,
            account_key=account_key,
            container_name=container_name,
            blob_name=blob_name,
            permission=sas_permissions,
            expiry=expiry_time,
            start=start_time
        )

        return sas_token

    def create_url_with_saskey(self, account_name: str, account_key: str, container_name: str, blob_name: str):
        # Generate the SAS token for the specific blob
        sas_token = self.create_blob_sas(account_name, account_key, container_name, blob_name)

        # Construct the blob URL with the SAS token
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"

        return blob_url
