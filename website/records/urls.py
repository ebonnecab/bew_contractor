from django.urls import path
from records.views import RecordsListView


urlpatterns = [
    path('', RecordsListView.as_view(), name='index'),
]