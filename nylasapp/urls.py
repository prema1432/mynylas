from django.urls import path
from .views import read_emails, handle_authorization, start_authorization, micro_start_authorization, \
    yahoo_start_authorization, send_email, all_nylas_accounts

urlpatterns = [
    path('read-emails/', read_emails, name='read_emails'),
    path('start-authorization/', start_authorization, name='start_authorization'),
    path('micro-authorization/', micro_start_authorization, name='micro_start_authorization'),
    path('yahoo-authorization/', yahoo_start_authorization, name='yahoo_start_authorization'),
    path('handle-authorization/', handle_authorization, name='handle_authorization'),
    path('send_email/', send_email, name='send_email'),
    path('', all_nylas_accounts, name='all_nylas_accounts'),

]