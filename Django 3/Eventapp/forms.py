from django import forms

class EventForm(forms.Form):
    field1 = forms.CharField(label='Event Name', max_length=100)
    field2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Participants',max_length=100)
    field3 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Place',max_length=100)
    field4 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Description',max_length=100)