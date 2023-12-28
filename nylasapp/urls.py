from django.urls import path
from .views import read_emails, handle_authorization, start_authorization, micro_start_authorization, \
    yahoo_start_authorization

urlpatterns = [
    path('read-emails/', read_emails, name='read_emails'),
    path('start-authorization/', start_authorization, name='start_authorization'),
    path('micro-authorization/', micro_start_authorization, name='micro_start_authorization'),
    path('yahoo-authorization/', yahoo_start_authorization, name='yahoo_start_authorization'),
    path('handle-authorization/', handle_authorization, name='handle_authorization'),

]