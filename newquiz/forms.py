from django import forms

class PassForm(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email
