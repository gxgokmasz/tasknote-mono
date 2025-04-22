import inject
from django import forms
from django.core.exceptions import ValidationError

from ...application.dtos import UserLoginDTO


class AuthenticationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput({"class": "input-field input-default"}),
        label="Nome de usuário ou Email",
    )
    password = forms.CharField(
        widget=forms.PasswordInput({"class": "input-field input-default"}), label="Senha"
    )

    def __init__(self, *args, **kwargs) -> None:
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)

    def clean(self) -> dict:
        cleaned_data = self.cleaned_data

        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            user = UserLoginDTO(username, password)
            authenticate_user_use_case = inject.instance("AuthenticateUserUseCase")
            authenticated_user = authenticate_user_use_case.execute(user, self.request)

            if not authenticated_user:
                raise ValidationError("Nome de usuário e/ou senha inválidos.")

        return cleaned_data
