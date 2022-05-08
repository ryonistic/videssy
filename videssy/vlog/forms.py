from django import forms
from .models import Video, Comment 


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail', 'footage' )


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
