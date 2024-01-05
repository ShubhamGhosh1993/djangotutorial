from django import forms

class UserForm(forms.Form):
    email = forms.CharField(label="Email",required=True,widget=forms.TextInput(attrs={'class': 'classs1'}))
    name = forms.CharField(label="Name",required=True,widget=forms.TextInput(attrs={'class': 'name1'}))