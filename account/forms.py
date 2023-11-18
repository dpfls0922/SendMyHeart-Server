from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserBasedForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

class UserCreateForm(UserBasedForm):
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta(UserBasedForm.Meta):
        fields = ['email', 'password', 'phone']

class SignUpForm(UserCreationForm):
    class Meta(UserCreateForm.Meta): # UserCreateForm에서 변경
        model = get_user_model()
        fields=['email', 'phone']

class LoginForm(forms.Form):
    email = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "이메일"})
    )
    password = forms.CharField(
        max_length=30, required=True, widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "패스워드"})
    )