from django import forms
from django.core.mail import send_mail

class CanPass(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email


class ApplicationForm():
    full_name = forms.CharField(label="Full Name", max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    aptitude_score = forms.IntegerField(label='Aptitude Score',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Aptitude test score'}))
    degree = forms.ChoiceField(choices=[('be_btech','BE/B.Tech'),('bsc','B.Sc'),('msc','M.Sc'),('me_mtech','ME/M.Tech')])
    degree_score = forms.IntegerField(label='Degree Score',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Degree score in percentage without adding sign %'}))
