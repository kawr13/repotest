from django import forms
from CabinetApp.models import Record

class RecordsForms(forms.ModelForm):
    title = forms.CharField()
    url = forms.URLField()

    class Meta:
        model = Record
        fields = ['title', 'url', 'cabinet']

