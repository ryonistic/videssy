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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class']='p-2 m-2 rounded border'
        self.fields['content'].widget.attrs['placeholder']='Enter Comment'


