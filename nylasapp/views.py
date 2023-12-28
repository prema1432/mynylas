import json

from django.shortcuts import render, redirect

import requests
from django.http import HttpResponse
import nylas

from nylas_sample.settings import NYLAS_CLIENT_ID, NYLAS_CLIENT_SECRET
from nylas_sample.utils import get_nylas_access_token


def read_emails(request):
    nyls_access_token = get_nylas_access_token(NYLAS_CLIENT_ID, NYLAS_CLIENT_SECRET)
    print("access_tokenaccess_tokenaccess_token", nyls_access_token)
    # Initialize Nylas client
    nylas_client = nylas.APIClient(
        client_id=NYLAS_CLIENT_ID,
        client_secret=NYLAS_CLIENT_SECRET,
        access_token=nyls_access_token

    )
    return HttpResponse(f'Inbox Emails:<br>{nylas_client}')
    # # Example: Read emails from the inbox
    # messages = nylas_client.messages.all()
    # print("messages",messages)
    # inbox_emails = [{'subject': message.subject, 'body': message.body} for message in messages]
    #
    # # Render the emails in a simple HTML format
    # email_list = "<br>".join([f"<b>{email['subject']}</b>: {email['body']}" for email in inbox_emails])
    #
    # return HttpResponse(f'Inbox Emails:<br>{email_list}')


def start_authorization(request):
    # Construct the authorization URL
    redirect_uri = 'https://mynylass.onrender.com/handle-authorization/'  # Change to your desired URL
    print("redirect_uri",redirect_uri)
    authorization_url = (
        f'https://api.nylas.com/oauth/authorize?'
        f'client_id={NYLAS_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code&login_hint=premanath@myyahoo.com'
    )
    print("authorization_url",authorization_url)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.request("GET", authorization_url, headers=headers, data=payload)

    print('fhjsdgfjgskd fghjksdghj',response.json())

    # Redirect the user to the Nylas authorization URL
    return redirect(authorization_url)

def micro_start_authorization(request):
    host_name = request.get_host()
    print(":host_name",host_name)
    if 'HTTP_X_FORWARDED_PROTO' in request.META:
        protocol = request.META['HTTP_X_FORWARDED_PROTO']
    else:
        # If the header is not present, use the scheme attribute
        protocol = request.scheme

    print("protocolprotocolprotocol",protocol)

    # Construct the authorization URL
    redirect_uri = f'{protocol}://{host_name}/handle-authorization/'  # Change to your desired URL
    print("redirect_uri",redirect_uri)
    authorization_url = (
        f'https://api.nylas.com/oauth/authorize?'
        f'client_id={NYLAS_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code&login_hint=talamarlapremanath143@gmail.com'
    )
    print("authorization_url",authorization_url)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.request("GET", authorization_url, headers=headers, data=payload)

    print('fhjsdgfjgskd fghjksdghj',response.json())

    # Redirect the user to the Nylas authorization URL
    return redirect(authorization_url)

def yahoo_start_authorization(request):
    host_name = request.get_host()
    print(":host_name",host_name)
    if 'HTTP_X_FORWARDED_PROTO' in request.META:
        protocol = request.META['HTTP_X_FORWARDED_PROTO']
    else:
        # If the header is not present, use the scheme attribute
        protocol = request.scheme

    print("protocolprotocolprotocol",protocol)

    # Construct the authorization URL
    redirect_uri = f'{protocol}://{host_name}/handle-authorization/'  # Change to your desired URL
    print("redirect_uri",redirect_uri)
    authorization_url = (
        f'https://api.nylas.com/connect/authorize')
    print("authorization_url",authorization_url)
    payload = json.dumps({
        "client_id": NYLAS_CLIENT_ID,
        "name": "premanath",
        "email_address": "premanath@myyahoo.com",
        "provider": "yahoo",
        "settings": {
            "password": "Prema@143"
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.request("POST", authorization_url, headers=headers, data=payload)

    print('fhjsdgfjgskd fghjksdghj',response.json())

    # Redirect the user to the Nylas authorization URL
    return redirect(authorization_url)


def handle_authorization(request):
    print("requessssss",request)
    print("requessssss",request.data)
    # Handle the authorization code received from Nylas and exchange it for an access token
    authorization_code = request.GET.get('code')
    # ... perform the token exchange and other logic ...

    # Example: Display the authorization code (remove this in a production environment)
    return HttpResponse(f'Authorization Code: {authorization_code}')

