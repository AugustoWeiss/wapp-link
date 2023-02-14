from django import forms


class CreateNewLink(forms.Form):
    phone = forms.CharField(label="Phone", max_length=12)
    message = forms.CharField(widget=forms.Textarea)
