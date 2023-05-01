from django.urls import path 
from .views import * 

app_name = 'fahrasah' 

urlpatterns = [
    path('', all_projects, name='all-projects'),
    path('add-project/', add_project, name='add-project'),
    path('<int:project_id>/add-page/', add_page, name='add-page'), 
    path('<int:project_id>/add-field/', add_field, name='add-field'), 
    path('<int:id>/', project, name='single-project'),
    path('del/<int:id>', del_project, name='del-project'),
    path('del-page<int:id>/', del_page, name='del-page'),
    path('del-field/<int:id>/', del_field, name='del-field'), 
    path('del_duplicates/<str:field>', del_duplicated_projects, name='del-duplicated-projects'),
    path('del_duplicated_pages/<int:id>/', del_duplicated_pages, name='del-duplicated-pages'),
    path('del_duplicated_fields/<int:id>/', del_duplicated_fields, name='del-duplicated-fields'),

    path('project/edit/<int:id>/', edit_project, name='edit-project'), 
    path('page/edit/<int:id>/', edit_page, name='edit-page'), 
    path('field/edit/<int:id>/', edit_field, name='edit-field'), 

    path('services/remove-repeated/', remove_repeated_text, name='remove-repeated-text'),
    path('services/remove-repeated-record/<int:id>/', delete_repeated_text_record, name='remove-repeated-text-record')
]