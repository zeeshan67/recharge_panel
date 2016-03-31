__author__ = 'viva'


from django import forms


class UserForms(forms.Form):
    user_id = forms.CharField(max_length=256,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))