from django import forms
from records.models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'