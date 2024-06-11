from django import forms
from django.contrib.auth.forms import UserCreationForm
from players.models import Match, Player, Field


class MatchForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        label='Date'
    )

    start_hour = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}),
        label='Start time'
    )

    end_hour = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}),
        label='End time'
    )

    class Meta:
        model = Match
        fields = ['start_date', 'start_hour', 'end_hour', 'field', 'number_of_slots', 'price']

    def clean(self):
        cleaned_data = super().clean()
        start_hour = cleaned_data.get('start_hour')
        end_hour = cleaned_data.get('end_hour')

        if start_hour and end_hour and start_hour >= end_hour:
            raise forms.ValidationError("End hour must be after start hour.")

        return cleaned_data


# class MatchUpdateForm(forms.ModelForm):
#     start_date = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         input_formats=['%Y-%m-%d'],
#         label='Date'
#     )
#
#     start_hour = forms.TimeField(
#         widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}),
#         label='Start time'
#     )
#
#     end_hour = forms.TimeField(
#         widget=forms.TimeInput(attrs={'type': 'time', 'step': '1800'}),
#         label='End time'
#     )
#
#     class Meta:
#         model = Match
#         fields = ['start_date', 'start_hour', 'end_hour', 'field', 'number_of_slots', 'price']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         start_hour = cleaned_data.get('start_hour')
#         end_hour = cleaned_data.get('end_hour')
#
#         if start_hour and end_hour and start_hour >= end_hour:
#             raise forms.ValidationError("End hour must be after start hour.")
#
#         return cleaned_data


class PlayerForm(UserCreationForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'email', 'username']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'


class FieldUpdateForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'
