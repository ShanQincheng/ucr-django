from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit: bool = True) -> User:
        user = super().save(commit=False)
        # encrypt password from plain text to hashed text
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
