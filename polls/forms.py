from django import forms

from .models import Operation

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ('operation_text', 'operation_summa')
        

