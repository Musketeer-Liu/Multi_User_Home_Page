from django import forms
from .models import Post, Comment




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        # fields = ('author', 'title', 'text',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor_textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"
        # fileds = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor_textarea postcontent'})
        }
