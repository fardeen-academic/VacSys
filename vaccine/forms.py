from django import forms
from .models import Member


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'nid',
            'first_name',
            'last_name',
            'birth_date',
            'phone',
        )


class VaccineRegister(forms.Form):
    nid = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateField()
    phone = forms.IntegerField()


class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'nid',
            'first_name',
            'last_name',
            'birth_date',
            'phone',
            'first_dose_date',
            'first_dose_done',
            'second_dose_date',
            'second_dose_done',
        )


class MemberUpdate(forms.Form):
    nid = forms.IntegerField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    birth_date = forms.DateField()
    phone = forms.IntegerField()
    first_dose_date = forms.DateField()
    first_dose_done = forms.BooleanField()
    second_dose_date = forms.DateField()
    second_dose_done = forms.BooleanField()



