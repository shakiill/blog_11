from django import forms

from apps.front.models import Contact


class ContactForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Contact
        fields = "__all__"
