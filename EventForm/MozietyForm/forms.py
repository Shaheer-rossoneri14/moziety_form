from django import forms
from .models import Person
from django.forms import ModelForm

class Event_registration_form(ModelForm):
    email=forms.EmailField()    #widget=forms.EmailInput(attrs={'style': 'border-color: #ff9933;'}))
    name=forms.CharField()
    usn=forms.CharField()
    semester=forms.ChoiceField(choices=(('1','1'),('2','2'),('3','3'),('4','4'), ('5','5'), ('6','6'),('7','7'),('8','8')))
    dept=forms.ChoiceField(choices=(('CSE','CSE'),('ISE','ISE'),('ECE','ECE'),('AI&ML','AI&ML'), ('AI&DS','AI&DS'), ('EEE','EEE'),('ME','ME'),('CV','CV'),('Basic Science','Basic Science')))
    phone_number=forms.CharField()
    class Meta:
        model=Person
        fields='__all__'