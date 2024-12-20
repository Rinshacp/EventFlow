from django import forms
from django.forms import ModelForm
from .models import *

class clubform(ModelForm):
    class Meta:
        model=clubtable
        fields=[
            'name',
            'place',
            'post',
            'pin',
            'phoneno',
            'email',

        ]
class Updateclubform(ModelForm):
    class Meta:
        model=clubtable
        fields=[
            'name',
            'place',
            'post',
            'pin',
            'phoneno',
            'email',

        ]


class schoolform(ModelForm):
    class Meta:
        model=schooltable
        fields=[
            'name',
            'place',
            'post',
            'pin',
            'phoneno',
            'email',

        ]

class Updateschoolform(forms.ModelForm):
    class Meta:
        model = schooltable
        fields = [
            'name',
            'place',
            'post',
            'pin',
            'phoneno',
            'email',
        ]

class collegeform(ModelForm):
    class Meta:
        model=collegetable
        fields=[
            'name',
            'place',
            'post',
            'pin',
            'phoneno',
            'email',

        ]
class Updatecollegeform(ModelForm):
    class Meta:
        model=collegetable
        fields=[
            'name',
            'place',
            'post',
            'pin',
            'phoneno',
            'email',

        ]
class notificationform(ModelForm):
    class Meta:
        model=NotificationTable
        fields=[
            'notification',
        ]
class viewservicesform(ModelForm):
    class Meta:
        model=servicetable
        fields=[
            'services',
            'description',
        ]
class feedbackform(ModelForm):
    class Meta:
        model=feedback
        fields=['USER',
            'feedback',
        ]
class complaintsform(ModelForm):
    class Meta:
        model=complaints
        fields=['USER',
            'complaints',
        ]
class viewinstructionsform(ModelForm):
    class Meta:
        model=event
        fields=['eventname',
            'description',
        ]
class addstudentsform(ModelForm):
    class Meta:
        model=addstudents
        fields=['name',
                'course',
                'semester',
                'phoneno',
                'email',
                'CLUB_ID',
        ]