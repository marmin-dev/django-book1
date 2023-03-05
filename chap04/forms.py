from django import forms
from .validator import validate_com


class ContactForm(forms.form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(validators=[validate_com])
    cc_myself = forms.BooleanField(required=False)
