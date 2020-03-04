from django.urls import path
from records.views import RecordsListView, RecordsDetailView, RecordsCreateView

urlpatterns = [
    path('', RecordsListView.as_view(), name='index'),
    path('new/', RecordsCreateView.as_view(), name='new'),
    path('<int:pk>/', RecordsDetailView.as_view(), name='detail'),

]