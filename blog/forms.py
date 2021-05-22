from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Blog
from bootstrap_datepicker_plus import DatePickerInput

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("first_name", "last_name","username", "email", "password1", "password2")
        
        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.first_name = self.cleaned_data["first_name"]
            user.last_name = self.cleaned_data["last_name"]
            user.email = self.cleaned_data['email']
            
            if commit:
                user.save()
            return user

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        # fields = "__all__"
        exclude = ('author',)
        widgets = {
            'date_published': DatePickerInput(format='%Y-%m-%d'),
        }


form = Blog()