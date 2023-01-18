from django.contrib.auth.forms import PasswordChangeForm
from django import forms
from .models import Room, Message, Topic


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ("topic", "name", "description")


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("content",)
        widgets = {}


