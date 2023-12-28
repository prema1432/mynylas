from django import forms

from nylasapp.models import UserAccount


class UserAccountForm(forms.Form):
    user_account = forms.ModelChoiceField(
        queryset=UserAccount.objects.filter(status="running"),
        empty_label=None,
        to_field_name='email_address',
        label='Select User Account'
    )
