from django import forms
from fashionpointapp.models import Post,Category,UserProfile
from django.contrib.auth.models import User
from django.forms.widgets import DateInput


class UserForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password')
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password do not match")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','dateOfBirth')
        labels = {
            'dateOfBirth': 'Date of Birth',
        }
        widgets = {
            'dateOfBirth': DateInput(attrs={'type': 'date'})

        }
class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)
    description = forms.CharField(max_length=128,required=False)
    photo = forms.ImageField()
    avgRating = forms.FloatField(widget=forms.HiddenInput(),required=False,initial=0)
    date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Post
        fields=['photo','description','category']