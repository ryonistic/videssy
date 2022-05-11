"""
For creation of videos and comments, one needs to fill all required
fields. This data is then saved to the database. As DBMS doesnt save videos
directly, it actually saves the address of the video and puts the video in a media
root folder that is predecided by the model or the settings.py file
"""
from django import forms
from .models import Video, Comment 


class CreateVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail', 'footage', 'tag' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs['class']='p-2 m-2 rounded border'
            self.fields[fieldname].widget.attrs['placeholder']=str((fieldname).upper())


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs['class']='p-2 m-2 rounded border'
        self.fields['content'].widget.attrs['placeholder']='Enter Comment'


