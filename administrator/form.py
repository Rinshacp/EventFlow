from django import forms
from django.forms import ModelForm
from administrator.models import clubtable, collegetable, feedback, notificationtable, schooltable, servicetable 


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
        model=notificationtable
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
        fields=[
            'feedback',
        ]


class ClubRegistrartionForm(ModelForm):
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
