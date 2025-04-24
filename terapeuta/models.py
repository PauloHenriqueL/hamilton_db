from django.db import models
from django.core.validators import RegexValidator
from decano.models import Decano


class Terapeuta(models.Model):
    
#   Modelo para cadastrar terapeutas no sistema.

    nome = models.CharField(
        max_length=200, 
        verbose_name="Nome Completo",
    )

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name="Email",
    )

    telefone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="O número de telefone deve estar no formato: '+999999999'. Até 15 dígitos permitidos."
            )
        ],
        verbose_name="Telefone de Contato"
    )
    
    OPCOES_SEXO = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    
    sexo = models.CharField(
        max_length=2,
        choices=OPCOES_SEXO,
        verbose_name="Sexo"
    )
    
    OPCOES_ABORDAGEM = [
        ('TCC', 'Cognitivo-Comportamental'),
        ('PSC', 'Psicanálise'),
        ('HUM', 'Humanista'),
        ('ANA', 'Analítica'),
    ]
    
    abordagem = models.CharField(
        max_length=3,
        choices=OPCOES_ABORDAGEM,
        verbose_name="Abordagem Terapêutica"
    )
    
    estado = models.CharField(
        max_length=2,
        verbose_name="Estado (UF)"
    )
    
    OPCOES_NUCLEO = [
        ('Jungiano', 'Jungiano'),
        ('Humanista', 'Humanista'),
        ('Cognitivo-Comportamental', 'Cognitivo-Comportamental'),
        ('Neuro', 'Neuro'),
        ('Social', 'Social'),
        ('Psicanálise', 'Psicanálise'),
        ('Formação Clássica', 'Formação Clássica'),
    ]
    
    nucleo = models.CharField(
        max_length=200,
        choices=OPCOES_NUCLEO,
        verbose_name="Núcleo"
    )
    
    cidade = models.CharField(
        max_length=100,
        verbose_name="Cidade"
    )
    
    decano = models.ForeignKey(
        Decano,
        on_delete=models.PROTECT,
        related_name='terapeutas',
        null=True,
        blank=True,
        verbose_name="Decano Responsável"
    )
    
    OPCOES_CLINICA = [
        ('ESC', 'Clínica Escola'),
        ('ALL', 'Clínica Allos'),
        ('PAR', 'Parceria'),
    ]
    
    clinica = models.CharField(  # Corrigido o nome do campo (removido acento)
        max_length=3,
        choices=OPCOES_CLINICA,
        verbose_name="Clínica"
    )
    
    OPCOES_MODALIDADE = [
        ('PRES', 'Presencial'),
        ('ONL', 'Online'),
        ('HIB', 'Híbrido')
    ]
    
    modalidade = models.CharField(
        max_length=4,
        choices=OPCOES_MODALIDADE,
        verbose_name="Modalidade de Atendimento"
    )
    
    OPCOES_FAIXA_ETARIA = [
        ('INF', 'Infantil'),
        ('ADO', 'Adolescente'),
        ('ADU', 'Adulto'),
        ('IDO', 'Idoso'),
        ('TOD', 'Todas')
    ]
    
    prefeidade = models.CharField(  # Renomeado para preferencia_idade para maior clareza
        max_length=3,
        choices=OPCOES_FAIXA_ETARIA,
        verbose_name="Preferência de Faixa Etária"
    )

    disponibilidade = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="Disponibilidade de Horários",
        help_text="Dias e horários disponíveis para atendimento"
    )
    
    ativo = models.BooleanField(
        default=True,
        verbose_name="Terapeuta Ativo",
        help_text="Indica se o terapeuta está ativo no sistema"
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
        verbose_name = 'Terapeuta'
        verbose_name_plural = 'Terapeutas'
        ordering = ['nome']

    def __str__(self):
        return self.nome
