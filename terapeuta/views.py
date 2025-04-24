from rest_framework import generics
from terapeuta.models import Terapeuta
from terapeuta.serializers import TerapeutaSerializer


class TerapeutaCreateListView(generics.ListCreateAPIView):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer


class TerapeutaRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer
