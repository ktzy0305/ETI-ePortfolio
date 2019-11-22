from django import forms

class CommentForm(forms.Form):
    body = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "name": "body",
                "id" : "comment_body",
                "placeholder": "Leave a comment!"
            })
    )