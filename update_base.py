import os
import requests
import json
from requests_toolbelt import MultipartEncoder

class LarkSuiteCredentialsFetcherupload:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        url = 'https://open.larksuite.com/open-apis/auth/v3/tenant_access_token/internal'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'app_id': self.app_id,
            'app_secret': self.app_secret
        }
        print("Waiting for response from lark base")
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
        print("Response Recieved")
        return response.json()['tenant_access_token']
    


    def update_specific_cell(self,  record_id, recor_value, tbl_id, base_id):
        url = f'https://open.larksuite.com/open-apis/bitable/v1/apps/{base_id}/tables/{tbl_id}/records/batch_update'
        
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        
        data = {
            "records":[
                {
                    "record_id": record_id,
                    "fields": {
                        'email_send_status':recor_value,
                        
                    }
                }
            ]

        }

        print("Updating specific cell in Lark base table")
        response = requests.post(url=url, headers=headers, data=json.dumps(data))
        print("Cell updated")
        return response.json()
    

def upload_invoic_to_base(record_id, base_id, tbl_id):

    app_id = 'cli_a47dc8d4f0f89009'
    app_secret = 'G7z7VHsyXOA6reIX1NujucUNSICcjL6v'
    record_id = record_id  # Replace with your record id

    recor_value = True

    lark_suite = LarkSuiteCredentialsFetcherupload(app_id, app_secret)

    response = lark_suite.update_specific_cell(
        record_id = record_id ,
        recor_value = recor_value,
        base_id = base_id,
        tbl_id= tbl_id
    )

    print(response)