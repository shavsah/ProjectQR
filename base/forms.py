from django.forms import ModelForm
from base.models import PersonalData


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address']
