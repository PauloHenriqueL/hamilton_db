from rest_framework import generics
from decano.models import Decano
from decano.serializers import DecanoSerializer


class DecanoCreateListView(generics.ListCreateAPIView):
    queryset = Decano.objects.all()
    serializer_class = DecanoSerializer


class DecanoRetrieveUpdateDestoyView(generics.RetrieveDestroyAPIView):
    queryset = Decano.objects.all()
    serializer_class = DecanoSerializer
