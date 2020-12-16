#Django
from django import forms
#models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    #sginup Forms
    username = forms.CharField(min_length=4, max_length=20,required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Username',
                                    'autocomplete': 'off',
                                    }))
    password = forms.CharField(max_length=70, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password',
                                    'autocomplete': 'off',
                                    }))
    password_confirmation = forms.CharField(max_length=70, required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password confirmation',
                                    'autocomplete': 'off',
                                    }))

    first_name = forms.CharField(min_length=2, max_length=50, required=True,
                                 widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Fist Name',
                                    'autocomplete': 'off',
                                    }))
    last_name = forms.CharField(min_length=2, max_length=50, required=True,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Last Name',
                                    'autocomplete': 'off',
                                    }))
    email = forms.EmailField(min_length=6, max_length=30, required=False,
                                widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Email',
                                    'autocomplete': 'off',
                                    }))

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()

class ProfileForm(forms.Form):
    #Profile forms
    website = forms.URLField(max_length=200 , required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
