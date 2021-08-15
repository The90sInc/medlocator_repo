from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import fields
from .models import Pharmacy

class PharmacyForm(forms.ModelForm):
    name = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"placeholder": "Pharmacy Name"}))
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email', widget=forms.TextInput(attrs={"placeholder": "Email"}))
    account_manager = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Account Manager First and last name"}))
    account_manager_phone_number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Account manager phone number"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Retype Password"}))
    accept_terms = forms.BooleanField(widget=forms.CheckboxInput())

    class Meta:
        model = Pharmacy
        exclude = ["created_at","created_by"]


    def clean(self):
        cleaned_data = super(PharmacyForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'password and confirm_password does not match'
            )

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    accept_terms = forms.BooleanField(widget=forms.CheckboxInput())
    account_manager = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Account Manager First and Last Name"}))
    account_manager_phone_number = forms.IntegerField(widget=forms.TextInput(attrs={"placeholder": "Account manager phone number"}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields +('username','account_manager', 'email','account_manager_phone_number', 'password1','password2','accept_terms')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Pharmacy Name'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype Password'
