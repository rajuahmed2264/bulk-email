import json
import requests

class LarkSuiteCredentialsFetcher:
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

    def fetch_credentials(self, base_id, tbl_id):
        all_items = []
        url = f'https://open.larksuite.com/open-apis/bitable/v1/apps/{base_id}/tables/{tbl_id}/records'
        headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        params = {
            'view_id': 'vewvG5sfbY',
            'field_names': '["Restaurant Name", "email", "email_send_status"]',
            'page_size': 500  # Hypothetical, check the API documentation for the correct parameter
        }
        print("Getting lark base data")

        while True:
            
            response = requests.get(url, headers=headers, params=params)
            data = response.json()

            items = data['data']['items']
            if items != None:
                all_items.extend(items)
            else:
                break

            # Check for pagination token or cursor (this is hypothetical, check the API documentation)
            next_page_token = data['data'].get('page_token', '')
            if next_page_token !='':
                params['page_token'] = next_page_token  # Hypothetical, check the API documentation for the correct parameter
            else:
                break
        return all_items

def get_data_from_base_f(base_id, tbl_id):
    app_id = 'cli_a47dc8d4f0f89009'
    app_secret = 'G7z7VHsyXOA6reIX1NujucUNSICcjL6v'

    credentials_fetcher = LarkSuiteCredentialsFetcher(app_id, app_secret)
    all_rows = credentials_fetcher.fetch_credentials(base_id, tbl_id)
    actual_row = all_rows

    return actual_row