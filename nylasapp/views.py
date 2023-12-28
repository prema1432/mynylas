import json

from django.shortcuts import render, redirect

import requests
from django.http import HttpResponse
import nylas

from nylas_sample.settings import NYLAS_CLIENT_ID, NYLAS_CLIENT_SECRET
from nylas_sample.utils import get_nylas_access_token
from nylasapp.forms import UserAccountForm
from nylasapp.models import UserAccount


# def read_emails(request):
#
#     nyls_access_token = "i5BxeE9hjhWiji2CQhxdNdGKhc5jD5"
#     # print("access_tokenaccess_tokenaccess_token", nyls_access_token)
#     nylas_client = nylas.APIClient(
#         client_id=NYLAS_CLIENT_ID,
#         client_secret=NYLAS_CLIENT_SECRET,
#         access_token=nyls_access_token
#
#     )
#     email_list = nylas_client.messages.all()
#     inbox_emails = [
#         {
#             'subject': message.subject,
#             'date': message.date,
#             'from_mail': message.from_email,
#         }
#         for message in email_list
#     ]
#     return render(request, 'my_messages.html', {'email_list': inbox_emails})

def read_emails(request):
    # nylas_access_token = "i5BxeE9hjhWiji2CQhxdNdGKhc5jD5"
    # nylas_access_token = ""
    inbox_emails ={}

    errors= None
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            selected_email_address = form.cleaned_data['user_account']
            print("selected_email_addressselected_email_address",selected_email_address)
            # Retrieve all fields of the selected UserAccount object
            selected_user_account = UserAccount.objects.get(email_address=selected_email_address)
            # Update nylas_access_token based on the selected user account
            nylas_access_token = selected_user_account.access_token
            print("nylas_access_token",nylas_access_token)
            nylas_client = nylas.APIClient(
                client_id=NYLAS_CLIENT_ID,
                client_secret=NYLAS_CLIENT_SECRET,
                access_token=nylas_access_token
            )

            try:
                email_list = nylas_client.messages.all()
                print("email_list 876yijh" ,email_list)
                inbox_emails = [
                    {
                        'subject': message.subject,
                        'date': message.date,
                        'from_mail': message.from_email,
                    }
                    for message in email_list
                ]
            except Exception as e:
                errors =str(e)
                print("exception occured as",e)
        else:
            print(" uhkjhjkhjkhjkhkjh",form.errors)
    else:
        form = UserAccountForm()



    return render(request, 'my_messages.html', {'email_list': inbox_emails, 'form': form,"errors":errors})

# def start_authorization(request):
#     host_name = request.get_host()
#     print(":host_name", host_name)
#     if 'HTTP_X_FORWARDED_PROTO' in request.META:
#         protocol = request.META['HTTP_X_FORWARDED_PROTO']
#     else:
#         # If the header is not present, use the scheme attribute
#         protocol = request.scheme
#
#     print("protocolprotocolprotocol", protocol)
#
#     # Construct the authorization URL
#     redirect_uri = f'{protocol}://{host_name}/handle-authorization/'  # Change to your desired URL
#     print("redirect_uri", redirect_uri)
#     authorization_url = (
#         f'https://api.nylas.com/oauth/authorize?'
#         f'client_id={NYLAS_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code'
#     )
#     print("authorization_url", authorization_url)
#     payload = {}
#     headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#     }
#     response = requests.request("GET", authorization_url, headers=headers, data=payload)
#
#     print('fhjsdgfjgskd fghjksdghj', response.json())
#
#     # Redirect the user to the Nylas authorization URL
#     return HttpResponse(f'response: {response.json()}')
#     # return redirect(authorization_url)

def start_authorization(request):
    host_name = request.get_host()

    if 'HTTP_X_FORWARDED_PROTO' in request.META:
        protocol = request.META['HTTP_X_FORWARDED_PROTO']
    else:
        protocol = request.scheme

    redirect_uri = f'{protocol}://{host_name}/handle-authorization/'  # Change to your desired URL

    authorization_url = (
        f'https://api.nylas.com/oauth/authorize?'
        f'client_id={NYLAS_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code'
    )
    print("authorization_url",authorization_url)

    # Redirect the user to the Nylas authorization URL
    return redirect(authorization_url)

def micro_start_authorization(request):
    host_name = request.get_host()
    print(":host_name", host_name)
    if 'HTTP_X_FORWARDED_PROTO' in request.META:
        protocol = request.META['HTTP_X_FORWARDED_PROTO']
    else:
        # If the header is not present, use the scheme attribute
        protocol = request.scheme

    print("protocolprotocolprotocol", protocol)

    # Construct the authorization URL
    redirect_uri = f'{protocol}://{host_name}/handle-authorization/'  # Change to your desired URL
    print("redirect_uri", redirect_uri)
    authorization_url = (
        f'https://api.nylas.com/oauth/authorize?'
        f'client_id={NYLAS_CLIENT_ID}&redirect_uri={redirect_uri}&response_type=code&login_hint=talamarlapremanath143@gmail.com'
    )
    print("authorization_url", authorization_url)
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    response = requests.request("GET", authorization_url, headers=headers, data=payload)

    print('fhjsdgfjgskd fghjksdghj', response.json())

    # Redirect the user to the Nylas authorization URL
    return redirect(authorization_url)


def yahoo_start_authorization(request):
    host_name = request.get_host()
    print(":host_name", host_name)
    if 'HTTP_X_FORWARDED_PROTO' in request.META:
        protocol = request.META['HTTP_X_FORWARDED_PROTO']
    else:
        # If the header is not present, use the scheme attribute
        protocol = request.scheme

    print("protocolprotocolprotocol", protocol)

    # Construct the authorization URL
    redirect_uri = f'{protocol}://{host_name}/handle-authorization/'  # Change to your desired URL
    print("redirect_uri", redirect_uri)
    authorization_url = (
        f'https://api.nylas.com/connect/authorize')
    print("authorization_url", authorization_url)
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
    }
    response = requests.request("POST", authorization_url, headers=headers, data=payload)

    print('fhjsdgfjgskd fghjksdghj', response.json())

    # Redirect the user to the Nylas authorization URL
    return redirect(authorization_url)


def handle_authorization(request):
    print("requessssss", request)
    # print("requessssss", request.data)
    # Handle the authorization code received from Nylas and exchange it for an access token
    authorization_code = request.GET.get('code')
    access_data = ""
    try:
        url = f"https://api.nylas.com/oauth/token?client_id={NYLAS_CLIENT_ID}&client_secret={NYLAS_CLIENT_SECRET}&grant_type=authorization_code&code={authorization_code}"
        print("url",url)
        payload = ""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {authorization_code}'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        print("response",response)
        print("response",response.json())
        print("response",response.status_code)
        access_data =response.json()
        # print(response.text)
        try:
            # {'access_token': 'QGUCk8iK7c4iEWYqjAQ7dYyU4Pnph6', 'account_id': '8pc9hg23yko29vx57n58ne67h',
            #  'email_address': 'talamarla.premanath@gmail.com', 'provider': 'gmail', 'token_type': 'bearer'}
            lookup_field = 'email_address'
            email_address = access_data[lookup_field]

            defaults = {
                'access_token': access_data['access_token'],
                'account_id': access_data['account_id'],
                'provider': access_data['provider'],
                'token_type': access_data['token_type'],
            }

            user_account, created = UserAccount.objects.update_or_create(
                **{lookup_field: email_address},
                defaults=defaults
            )
            # UserAccount.objects.create()
        except Exception as e:
            print("Exception occureddownloading data",e)

    except Exception as e:
        print("Exception occured in the call back url",e)

    return HttpResponse(f'Authorization Code: {authorization_code}, Access Data:{access_data}')

def send_email(request):
    # nyls_access_token = "i5BxeE9hjhWiji2CQhxdNdGKhc5jD5"

    if request.method == 'POST':
        # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your actual Nylas API credentials

        #
        # nylas_client = nylas.APIClient(client_id=client_id, client_secret=client_secret)
        nylas_client = nylas.APIClient(
            client_id=NYLAS_CLIENT_ID,
            client_secret=NYLAS_CLIENT_SECRET,
            access_token=nyls_access_token

        )
        # Extract input from the form
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        try:
            # Create the draft message
            draft = nylas_client.drafts.create(
                to=[{'email': to_email}],
                subject=subject,
                body=body,
            )

            # Send the draft
            draft.send()

            message = "Email sent successfully."
        except Exception as e:
            message = f"Error sending email: {str(e)}"

        # Render the template with the message
        return render(request, 'send_email.html', {'message': message})

    # Render the initial form
    return render(request, 'send_email.html', {'message': None})