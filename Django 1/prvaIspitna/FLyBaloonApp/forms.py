from django import forms
from .models import Let

class LetForm(forms.ModelForm):
    def __init__(self, *args, ** kwargs):
        super(LetForm, self).__init__(*args, ** kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"
    class Meta:
        model = Let
        exclude = ['kreator',]