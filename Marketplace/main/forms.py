from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UpdateProfile(forms.ModelForm):
    age = forms.IntegerField()

    def clean_age(self):
        if self.cleaned_data['age'] < 18:
            raise ValidationError('Возвращайтесь когда вам исполнится 18 лет')
        return self.cleaned_data['age']

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

#
# class MailForm(forms.Form):
#     subject = forms.CharField(label='тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
