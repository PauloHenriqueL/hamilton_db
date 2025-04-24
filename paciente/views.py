from rest_framework import generics
from paciente.models import Paciente
from paciente.serializers import PacienteSerializer


class PacienteCreateViewList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class PacienteRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
