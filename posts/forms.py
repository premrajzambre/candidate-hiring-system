from django import forms
#from tinymce.widgets import TinyMCE
from .models import Post


"""class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False
"""

class PostForm(forms.ModelForm):
    """job_description = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    skills = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )"""

    class Meta:
        model = Post
        fields = ('blog_title', 'job_title', 'job_description', 
                'skills', 'author', 'thumbnail', 'featured',
                'experience', 'employment_type', 'vacancy',
                'job_status', 'previous_post', 'next_post',
                )
