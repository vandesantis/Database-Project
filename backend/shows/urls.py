from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', include('login.urls')),
    path('add_data/', include('add_data.urls')),
    path('<str:show_name>',views.detail),
]
