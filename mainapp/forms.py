from django import forms
from django.forms import ModelForm
from django.core.mail import send_mail
from .models import applicant
from posts.models import Post
from django.contrib.auth.models import User
from phone_field import PhoneField

def get_my_choices():
    def convert(list):
        return tuple(list)

    vc=Post.objects.filter(job_status__iexact='Active').values_list('job_title', flat=True)
    l=len(vc)
    ch= []
    for i in range(l):
        temp=(vc[i],vc[i])
        ch.append(temp)
    return convert(ch)

class mailsearch(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email

    def __init__(self, *args, **kwargs):
        super(mailsearch, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = "  Candidate's Email"
        self.fields['email'].label = 'Email'
        self.fields['email'].help_text = '<ul class="form-text small spantext"><li>Enter the email id of candidate.</li></ul>'

class ApplicationForm(ModelForm):
    class Meta:
        model = applicant
        fields = ('email', 'full_name', 'contact', 'degree', 'degree_score','type','job_post','aptitude_score')

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
        self.fields['contact'].help_text = '<ul class="form-text small spantext"><li>Write country code first.</li></ul>'

        self.fields['degree'].widget.attrs['class'] = 'form-control'
        #self.fields[''].widget.attrs['placeholder'] = 'Email'
        self.fields['degree'].label = 'Highest qualified degree  '

        self.fields['degree_score'].widget.attrs['class'] = 'form-control'
        #self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['degree_score'].label = 'Degree Score  '

        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['placeholder'] = '--choose--'
        self.fields['type'].label = 'I am  '

        self.fields['job_post'].widget.attrs['class'] = 'form-control'
        self.fields['job_post'].widget.attrs['placeholder'] = '---------'
        self.fields['job_post']=forms.ChoiceField(choices=get_my_choices() )
        self.fields['job_post'].label = 'Applying to  '
        self.fields['job_post'].help_text = '<ul class="form-text small spantext"><li>Enter the Post name for which you are applying.</li></ul>'

        self.fields['aptitude_score'].widget.attrs['class'] = 'form-control'
        self.fields['aptitude_score'].widget.attrs['placeholder'] = 'Enter test score'
        self.fields['aptitude_score'].label = 'Aptitude Score  '

class ApplicantSearchForm(ModelForm):
    #date_of_interview=forms.DateField()
    class Meta:
        model = applicant
        fields = ['hr_id']

    def __init__(self, *args, **kwargs):
        super(ApplicantSearchForm, self).__init__(*args, **kwargs)

        self.fields['hr_id'].widget.attrs['class'] = 'form-control'
        self.fields['hr_id'].widget.attrs['placeholder'] = ' HR ID'
        #self.fields['hr_id'].label = 'HR ID  '

class Salaryprediction(forms.Form):
    level = forms.IntegerField()

    def __str__(self):
        return self.level

def get_my_hr():
    def convert(list):
        return tuple(list)

    user = User.objects.all().values_list('username', flat=True)
    l=len(user)
    hr= []
    for i in range(l):
        temp=(user[i],user[i])
        hr.append(temp)
    return convert(hr)

class UpinfoForm(ModelForm):
    class Meta:
        model = applicant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UpinfoForm, self).__init__(*args, **kwargs)

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
        self.fields['contact'].help_text = '<ul class="form-text small spantext"><li>Write country code first.</li></ul>'

        self.fields['degree'].widget.attrs['class'] = 'form-control'
        #self.fields[''].widget.attrs['placeholder'] = 'Email'
        self.fields['degree'].label = 'Highest qualified degree  '

        self.fields['degree_score'].widget.attrs['class'] = 'form-control'
        #self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['degree_score'].label = 'Degree Score  '

        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['placeholder'] = '--choose--'
        self.fields['type'].label = 'I am  '

        self.fields['job_post'].widget.attrs['class'] = 'form-control'
        self.fields['job_post'].widget.attrs['placeholder'] = '---------'
        self.fields['job_post']=forms.ChoiceField(choices=get_my_choices() )
        self.fields['job_post'].label = 'Applying to  '
        self.fields['job_post'].help_text = '<ul class="form-text small spantext"><li>Enter the Post name for which candidate is applying.</li></ul>'

        self.fields['aptitude_score'].widget.attrs['class'] = 'form-control'
        self.fields['aptitude_score'].widget.attrs['placeholder'] = 'Enter test score'
        self.fields['aptitude_score'].label = 'Aptitude Score  '

        self.fields['technical_score'].widget.attrs['class'] = 'form-control'
        self.fields['technical_score'].widget.attrs['placeholder'] = 'Enter score'
        self.fields['technical_score'].label = 'Technical Score  '

        self.fields['personality_score'].widget.attrs['class'] = 'form-control'
        self.fields['personality_score'].widget.attrs['placeholder'] = 'Enter score'
        self.fields['personality_score'].label = 'Personality Score  '

        self.fields['average_score'].widget.attrs['class'] = 'form-control'
        #self.fields['personality_score'].widget.attrs['placeholder'] = 'Enter score'
        self.fields['average_score'].label = 'Average Score  '

        self.fields['hr_id'].widget.attrs['class'] = 'form-control'
        self.fields['hr_id'].widget.attrs['placeholder'] = '---------'
        self.fields['hr_id']=forms.ChoiceField(choices=get_my_hr() )
        self.fields['hr_id'].label = 'HR ID '
        self.fields['hr_id'].help_text = '<ul class="form-text small spantext"><li>Select your Username.</li></ul>'

        self.fields['date_of_interview'].widget.attrs['class'] = 'form-control'
        self.fields['date_of_interview'].label = 'Date'
        self.fields['date_of_interview'].help_text = '<ul class="form-text small spantext"><li>Enter the todays date in format "YYYY-MM-DD" e.g 2000-12-31. </li></ul>'
