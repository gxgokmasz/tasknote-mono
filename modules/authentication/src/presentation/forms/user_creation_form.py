from typing import Any

import inject
from django import forms
from django.core.exceptions import ValidationError

from ...application.dtos import UserCreateDTO
from ...domain.services import IUserValidationService
from ...infrastructure.models import User as UserModel
from ..validators import EmailValidator, PasswordValidator, UsernameValidator


class UserCreationForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput({"class": "input-field input-default"}),
        label="Nome de usuário",
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput({"class": "input-field input-default"}),
        label="Endereço de email",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            {"class": "input-field input-default", "autocomplete": "new-password"}
        ),
        label="Senha",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            {"class": "input-field input-default", "autocomplete": "new-password"}
        ),
        label="Confirmar senha",
    )

    @inject.autoparams()
    def __init__(self, user_validation_service: IUserValidationService, *args, **kwargs) -> None:
        self.request = kwargs.pop("request", None)

        super().__init__(*args, **kwargs)

        validate_username = UsernameValidator(user_validation_service)
        validate_email = EmailValidator(user_validation_service)

        self.fields["username"].validators.append(validate_username)
        self.fields["email"].validators.append(validate_email)

    @inject.autoparams()
    def clean_password2(self, user_validation_service: IUserValidationService) -> Any:
        cleaned_data = self.cleaned_data
        data = self.data

        username = data["username"]
        email = data["email"]
        password1 = cleaned_data["password1"]
        password2 = cleaned_data["password2"]

        if password1 != password2:
            raise ValidationError("As senhas não correspondem.")
        else:
            validate_password = PasswordValidator(user_validation_service)
            validate_password(password2, UserModel(username=username, email=email))

        return password2

    def clean(self) -> dict:
        cleaned_data = self.cleaned_data

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password2")

        if username and email and password:
            user = UserCreateDTO(username, email, password)
            create_user_use_case = inject.instance("CreateUserUseCase")
            create_user_use_case.execute(user, self.request)

        return cleaned_data
