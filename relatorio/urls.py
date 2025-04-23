from django.urls import path
from relatorio.views import RelatorioCrateListView, RelatorioRetrieveUpdateDestroyView


urlpatterns = [
    path('relatorio', RelatorioCrateListView.as_view(), name='relatorio-create-list'),
    path('relatorio/<int:pk>', RelatorioRetrieveUpdateDestroyView.as_view(), name='relatorio-detail-uptade'),
]
