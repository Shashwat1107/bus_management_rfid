from django import forms
from .models import Bus, Student

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['number', 'driver_name', 'driver_phone', 'start_point', 'end_point', 'via_points']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['register_number', 'bus']
