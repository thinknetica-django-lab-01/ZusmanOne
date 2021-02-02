from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UpdateProfile(forms.ModelForm):
    age=forms.IntegerField()

    def clean_age(self):
        if self.cleaned_data['age']<18:
            raise ValidationError('Возвращайтесь когда вам исполнится 18 лет')
        return self.cleaned_data['age']

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']