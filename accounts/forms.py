from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'nickname')

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('비밀번호가 같지 않습니다.')
        return super().clean()

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user
