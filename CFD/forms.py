from django import forms

class NameForm(forms.Form):
    fname = forms.CharField(label='First Name')
    lname = forms.CharField(label='Last Name')
    dob = forms.DateField(label='Date of Birth')