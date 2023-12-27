import requests

def get_nylas_access_token(client_id, client_secret, authorization_code, redirect_uri):
    try:
        oauth_url = 'https://api.nylas.com/oauth/token'
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': redirect_uri,
        }
        response = requests.post(oauth_url, data=data)
        response.raise_for_status()
        json_response = response.json()
        access_token = json_response.get('access_token')
        return access_token
    except Exception as e:
        print("Exception occurred:", e)
        return ""
# def get_nylas_access_token(client_id, client_secret):
#     try:
#         oauth_url = 'https://api.nylas.com/oauth/token'
#         data = {
#             "client_id": client_id,
#             "client_secret": client_secret,
#             "grant_type": 'client_credentials'
#         }
#         response = requests.post(oauth_url, data=data)
#         # print("Response Content:", response.text)
#         print("Response Status Code:", response.status_code)
#
#         print("responseresponse",response)
#         print("responseresponse",response)
#         print("responseresponse",response.json())
#         json_response = response.json()
#         access_token = json_response.get('access_token')
#         return access_token
#     except Exception as e:
#         print("exception occured as e", e)
#         return ""

