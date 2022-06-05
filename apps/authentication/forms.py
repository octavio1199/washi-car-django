# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "usuario",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "senha",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "usuario",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Senha",
                "class": "form-control"
            }
        ))
    """      # Para Adicionar
    # nome = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "nome",
    #             "class": "form-control"
    #         }
    #     ))
    # sobrenome = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "sobrenome",
    #             "class": "form-control"
    #         }
    #     ))
    # data_nascimento = forms.CharField(
    #     widget=forms.DateTimeField(
    #         attrs={
    #             "placeholder": "dd/mm/yyyy",
    #             "class": "form-control"
    #         }
    #     ))
    # telefone = forms.CharField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             "placeholder": "31-9 9999-9999",
    #             "class": "form-control"
    #         }
    #     ))
    # endereco = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "usuario",
    #             "class": "form-control"
    #         }
    #     ))
    # cep = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "usuario",
    #             "class": "form-control"
    #         }
    #     )) """
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # ['nome', 'sobrenome', 'data_nascimento', 'email',
        #           'telefone', 'endereco', 'cep']
