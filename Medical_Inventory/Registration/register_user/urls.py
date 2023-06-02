from django.urls import path
from .import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('register/',views.registration_view,name='register'),
    path('update/<str:registration_id>/', views.content_update_view, name='content_update'),
    path('success/',views.success,name='success'),
]
