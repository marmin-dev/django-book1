from django.db import models
from .validators import validate_com

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    sender = models.EmailField(validators=[validate_com])
    cc_myself = models.BooleanField(blank=True,null=True)