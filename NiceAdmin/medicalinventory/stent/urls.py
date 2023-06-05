from django.urls import path
from . import views
urlpatterns = [

    path('',views.medical_create.as_view(),name='api'),
    path('api/', views.MyModelListCreateView.as_view(), name='my-model-list-create'),
      path('api/get-data/', views.get_api_data, name='get-data'),
]