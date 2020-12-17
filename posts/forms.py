#post forms.

#django
from django import forms
#models
from posts.models import Post

class PostForm(forms.ModelForm):
    #Post Model Form.
    class Meta:
        #Form settings.
        model = Post
        fields = ('user', 'profile', 'title', 'photo')