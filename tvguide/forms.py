from django import forms
from .models import Program, Channel

class ProgramForm(forms.ModelForm):
    """Form for creating and updating Program instances."""
    channel = forms.ModelChoiceField(queryset=Channel.objects.all().order_by('name'))

    class Meta:
        model = Program
        fields = ['title', 'description', 'start_time', 'end_time', 'channel']
        widgets = {
            'start_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M' 
            ),
            'end_time': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        """
        Override init to format initial datetime values for the widgets
        if editing an existing instance.
        """
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            if self.instance.start_time:
                self.initial['start_time'] = self.instance.start_time.strftime('%Y-%m-%dT%H:%M')
            if self.instance.end_time:
                self.initial['end_time'] = self.instance.end_time.strftime('%Y-%m-%dT%H:%M')

    def clean(self):
        """
        Add custom validation, e.g., ensure end_time is after start_time.
        """
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")

        if start_time and end_time:
            if end_time <= start_time:
                raise forms.ValidationError("End time must be after start time.")
        return cleaned_data
    
# --- User Registration Form ---
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    """
    A form for registering new users, inheriting from Django's base.
    Includes username, password, and password confirmation fields by default.
    """

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields 

# --- Channel Form ---
class ChannelForm(forms.ModelForm):
    """Form for creating and updating Channel instances."""
    class Meta:
        model = Channel
        fields = ['name', 'country']