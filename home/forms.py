from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name" : "name",
                "maxlength" : 50,
                "placeholder": "Name"
            }
        )
    )

    email = forms.EmailField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "name" : "email",
                "maxlength" : 70,
                "placeholder": "Email",
                "type" : "email"
            }
        )
    )


    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "name" : "message",
                "maxlength" : 2000,
                "placeholder": "Message",
                "rows" : 9
            })
    )