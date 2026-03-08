from django import forms
from .models import Login

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    # username = forms.CharField(max_length=50, label='name', initial='enter user name', help_text='please enter your username')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput) 
    # password = forms.CharField(max_length=50, label='passcode') 
    email = forms.EmailField(max_length=254)
    # email = forms.EmailField(max_length=254, disabled=True, required=True)


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = Login
#         # fields = ['username', 'password']
#         fields = '__all__'