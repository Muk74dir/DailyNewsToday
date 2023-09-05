from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserRegistrationModel
from .constants import ACCOUNT_TYPE, GENDER_TYPE

class UserRegistrationFrom(UserCreationForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    phone_number = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'account_type', 'password1', 'password2', 'account_type', 'birth_date', 'gender', 'phone_number']

    def save(self, commit=True):
        temp_user = super().save(commit=False)
        if commit:
            temp_user.save()
            first_name = self.cleaned_data.get('first_name')
            last_name = self.cleaned_data.get('last_name')
            email = self.cleaned_data.get('email')
            account_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            birth_date = self.cleaned_data.get('birth_date')
            phone_number = self.cleaned_data.get('phone_number')

        
            UserRegistrationModel.objects.create(
                user=temp_user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                account_type=account_type,
                gender = gender,
                birth_date = birth_date,
                phone_number = phone_number,
            )

        return temp_user

