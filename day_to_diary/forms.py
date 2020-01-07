from django.forms import ModelForm
from .models import Input

class Entryform(ModelForm):
    class Meta:
        model=Input
        fields=('text',)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control'})  