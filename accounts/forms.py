from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from manager.models import Person

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	political_views = forms.CharField(max_length=50, required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2","political_views")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.political_views = self.cleaned_data['political_views']
		if commit:
			user.save()
		return user