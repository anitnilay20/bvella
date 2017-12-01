from django import forms
from users.models import users


class RegisterForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ('name', 'address', 'city', 'pincode', 'email', 'password', 'phno')

class LoginForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ('email','password')