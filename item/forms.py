from django import forms
from .models import Item, Category, ConversationMessage


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']


class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'label': '', 'class': 'form-control', 'placeholder': 'your message...'}), }


class MeepForm(forms.ModelForm):
    body = forms.CharField(max_length=150)

    class Meta:
        model = ConversationMessage
        fields = ('body',)
