from django.urls import path 
from .views import * 

app_name = 'duplicates_remover'

urlpatterns = [
    path('excel/', remove_duplicates_excel, name='remove-duplicates_excel')
]