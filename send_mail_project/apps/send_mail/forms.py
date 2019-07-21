from django import forms

#The new form

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )