from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from .models import applicant

class CanPass(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email


class ApplicationForm(ModelForm):
    class Meta:
        model = applicant
        fields = ('email', 'full_name', 'contact', 'degree', 'degree_score','type')

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = 'Email  '

        self.fields['full_name'].widget.attrs['class'] = 'form-control'
        self.fields['full_name'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['full_name'].label = 'Full Name  '
        self.fields['full_name'].help_text = '<ul class="form-text small spantext"><li>Start from first name.</li></ul>'

        #self.fields['contact'].widget.attrs['class'] = 'form-control'
        #self.fields['contact'].widget.attrs['placeholder'] = 'Contact Number'
        self.fields['contact'].label = 'Phone/Mobile '
        self.fields['full_name'].help_text = '<ul class="form-text small spantext"><li>Start from writing country code.</li></ul>'

        self.fields['degree'].widget.attrs['class'] = 'form-control'
        #self.fields[''].widget.attrs['placeholder'] = 'Email'
        self.fields['degree'].label = 'Highest qualified degree  '

        self.fields['degree_score'].widget.attrs['class'] = 'form-control'
        #self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['degree_score'].label = 'Degree Score  '

        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['placeholder'] = '--choose--'
        self.fields['type'].label = 'I am  '
