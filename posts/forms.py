from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

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

    job_description = forms.CharField(widget=CKEditorWidget())
    skills = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('blog_title', 'job_title', 'job_description', 
                'skills', 'author', 'thumbnail', 'featured',
                'experience', 'employment_type', 'vacancy',
                'job_status', 'previous_post', 'next_post',
                )
