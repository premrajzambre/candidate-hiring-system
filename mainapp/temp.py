def hr():
    user = User.objects.all().values_list('username', flat=True)
    return user

class UpdateForm(ModelForm):
    class Meta:
        model = applicant
        fields = ('email', 'full_name', 'contact', 'degree', 'degree_score','type','job_post','aptitude_score', 'technical_score', 'personality_score', 'average_score')

    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)

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

        self.fields['technical_score'].widget.attrs['class'] = 'form-control'
        self.fields['technical_score'].widget.attrs['placeholder'] = 'Enter score'
        self.fields['technical_score'].label = 'Technical Score  '

        self.fields['personality_score'].widget.attrs['class'] = 'form-control'
        self.fields['personality_score'].widget.attrs['placeholder'] = 'Enter score'
        self.fields['personality_score'].label = 'Personality Score  '

        self.fields['average_score'].widget.attrs['class'] = 'form-control'
        #self.fields['personality_score'].widget.attrs['placeholder'] = 'Enter score'
        self.fields['average_score'].label = 'Average Score  '

        """self.fields['hr_id'].widget.attrs['class'] = 'form-control'
        self.fields['hr_id'].widget.attrs['placeholder'] = '---------'
        self.fields['hr_id']=forms.ChoiceField(choices=hr() )
        self.fields['hr_id'].label = 'HR ID '
        self.fields['hr_id'].help_text = '<ul class="form-text small spantext"><li>Select your Username.</li></ul>'"""

        """self.fields['date_of_interview'].widget_attrs['class'] = 'form-control'
        self.fields['date_of_interview'].label = 'Date'"""