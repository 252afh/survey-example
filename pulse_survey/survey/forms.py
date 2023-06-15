from django import forms
from django.core.exceptions import ValidationError


def is_cabinet_office_email(email_address):
    if "@" not in email_address:
        raise ValidationError("Please supply a cabinet office email address, e.g. example@cabinetoffice.gov.uk", code="invalid-email",)
    split_email = email_address.split("@")
    email_domain = split_email[1]
    if email_domain == "cabinetoffice.gov.uk":
        return True
    else:
        raise ValidationError("Please supply a cabinet office email address, e.g. example@cabinetoffice.gov.uk", code="invalid-email",)
    

class FeedbackForm(forms.Form):
    template_name = "feedback.html"
    email = forms.EmailField(required=False, validators=[is_cabinet_office_email])
    content = forms.TextInput()

