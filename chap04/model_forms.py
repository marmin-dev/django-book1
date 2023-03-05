from django import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['subject', 'message', 'sender']
        # exclude = ['cc_myself']
        # fileds = '__all__'
