from django.urls import path
from registration.views import registration_view,success,content_update_view

urlpatterns = [
    path('', registration_view, name='registration'),
    #path('login/',login_view,{'registration_id': 'registration_id','registration_link': 'registration_link'},name='login'),
     path('update/<str:registration_id>/', content_update_view, name='content_update'),
    path('success/',success,name='success')
]
