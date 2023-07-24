from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from item.models import Item, Category


# for reference
# class SignUpF(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder':'inter your credential'}))

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'username',
#                'class': 'form-control',
#                }))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'placeholder': 'password',
#                'class': 'form-control',
#                }))


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username...'})}

    # username = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder': 'username...', 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'email...', 'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password...', 'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'repeat password...', 'class': 'form-control'}))


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'image', 'description', 'category', 'price')
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}), }

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'item name...', 'class': 'form-control'}))


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, )
