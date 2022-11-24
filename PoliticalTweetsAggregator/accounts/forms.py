from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomForm(UserCreationForm):
    # extra fields
    email = forms.EmailField(required=True)
    political_stance = forms.ChoiceField(
        choices=[('C', 'Conservatives'), ('L', 'Labour'), ('L-D', 'Liberal Democrats')])

    # extending the fields to include the two new fields

    class Meta:
        model = User
        fields = ("email", "username", "political_stance", "password1", "password2")

    # save the two new fields
    def save(self, commit=True):
        user = super(CustomForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.political_stance = self.cleaned_data["political_stance"]
        if commit:
            user.save()
        return user

