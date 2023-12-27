from django.urls import path
from .views import read_emails, handle_authorization, start_authorization

urlpatterns = [
    path('read-emails/', read_emails, name='read_emails'),
    path('start-authorization/', start_authorization, name='start_authorization'),
    path('handle-authorization/', handle_authorization, name='handle_authorization'),

]