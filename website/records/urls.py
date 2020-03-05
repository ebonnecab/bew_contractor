from django.urls import path
from records.views import RecordsListView, RecordsDetailView, RecordsCreateView, PatientsListView, PatientsDetailView, RecordsUpdateView, RecordsDeleteView

urlpatterns = [
    path('', RecordsListView.as_view(), name='index'),
    path('new/', RecordsCreateView.as_view(), name='new'),
    path('<int:pk>/update/', RecordsUpdateView.as_view(), name='records_update'),
    path('<int:pk>/delete/', RecordsDeleteView.as_view(), name='records_delete'),
    path('<int:pk>/', RecordsDetailView.as_view(), name='detail'),
    path('patients/', PatientsListView.as_view(), name='patient_list'),
    path('patients/<int:pk>/', PatientsDetailView.as_view(), name='patients_detail'),

]