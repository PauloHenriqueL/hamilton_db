from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class Decano(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )
    familia = models.CharField(
        max_length=200,
        verbose_name="Família"
    )
    email = models.EmailField(
        max_length=200,
        unique=True,
        validators=[EmailValidator()],
        verbose_name="E-mail"
    )
    telefone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O número de telefone deve estar no formato: '+999999999'. Máximo de 15 dígitos."
            )
        ],
        verbose_name="Telefone"
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name="Ativo"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Cadastro"
    )

    updated_at = models.DateTimeField(  # Corrigido nome do campo
        auto_now=True,
        verbose_name="Última Atualização"
    )

    class Meta:
        ordering = ['nome']
        verbose_name = 'Decano'

    def __str__(self):
        return self.nome
