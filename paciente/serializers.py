from rest_framework import serializers
from paciente.models import Paciente


class PacienteSerializer(serializers.ModelSerializer):
    model = Paciente
    fields = '__all__'
