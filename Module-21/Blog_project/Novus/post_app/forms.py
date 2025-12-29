# live-2
# we need form to create Post and comment


from django import forms
from .models import Post, Comment



# post form
# we need 4 fields of the Post model as input
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tag']                    # only these 4 fields needed




#comment form
# we need 1 field of the Comment model as input
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']                                                # only this 1 field needed

