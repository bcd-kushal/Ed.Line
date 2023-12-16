from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
                            max_length=100
                        )
    password = forms.CharField(
                            widget=forms.PasswordInput()
                        )




class SignupForm(forms.Form): 
    user = forms.CharField(max_length=100)   # mobile number: PK
    fname = forms.CharField(max_length=100)
    # lname = forms.CharField(max_length=100)
    email = forms.CharField(
                            max_length=100, 
                            widget=forms.EmailInput()
                        )
    pass1 = forms.CharField(
                            widget=forms.PasswordInput()
                        )


