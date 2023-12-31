from django.db import models

class UserAccount(models.Model):
    access_token = models.CharField(max_length=100)
    account_id = models.CharField(max_length=100)
    email_address = models.EmailField()
    provider = models.CharField(max_length=100)
    token_type = models.CharField(max_length=100)
    status= models.CharField(max_length=100,null=True,blank=True,default="stopped")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email_address
