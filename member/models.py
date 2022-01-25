from django.db import models

class Member(models.Model):
    user_id = models.CharField(max_length=50, unique=True, null=False)
    user_pw = models.CharField(max_length=50, null=False)
    user_name = models.CharField(max_length=50, null=False)
    date_joined = models.DateTimeField()