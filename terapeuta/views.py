from rest_framework import generics
from terapeuta.models import Terapeuta
from terapeuta.serializers import TerapeutaSerializer


class TerapeutaCrateListView(generics.ListCreateAPIView):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer
    

class TerapeutaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terapeuta.objects.all()
    serializer_class = TerapeutaSerializer