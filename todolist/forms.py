from django import forms

class ChoresForm(forms.Form):
    name = forms.CharField(label="Title", required=True, max_length=100)
    description = forms.CharField(label="Description", required=True)

class MarkedChoresForm(forms.Form):
    id = forms.CharField(label="id", required=True)
    is_finished = forms.BooleanField(label="isfinished", required=True)