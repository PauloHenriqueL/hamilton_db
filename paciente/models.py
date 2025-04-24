from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Paciente(models.Model):

#   Model para cadastrar pacientes no sistema.

    nome = models.CharField(max_length=200, verbose_name="Nome Completo", help_text="Nome completo do paciente")

    idade = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Idade")

    telefone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
            )
        ],
        verbose_name="Telefone de Contato",
    )

    contapoio = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
            )
        ],
        verbose_name="Telefone de Apoio",
    )

    valor_sessao = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Valor da Sessão",
    )

    OPCOES_SESSOES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    ]
    sessoes = models.CharField(
        max_length=2,
        choices=OPCOES_SESSOES,
        verbose_name="Quantidade de Sessões",
    )

    estrategia = models.CharField(
        max_length=15,
        verbose_name="Estratégia de venda",
    )

    preferencia = models.TextField(
        max_length=2000,
        verbose_name="Preferências e Observações",
        blank=True
    )

    ativo = models.BooleanField(
        default=True,
        verbose_name="Paciente Ativo",
        help_text="Indica se o paciente está ativo no sistema"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Cadastro"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última Atualização"
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
