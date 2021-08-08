from django import forms


class SubscriberForm(forms.Form):
    email = forms.EmailField(
        label="Email",
    )
