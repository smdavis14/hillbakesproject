from django.urls import path
from .views import index


app_name = 'hb'
urlpatterns = [
  path('', index, name='index'),
]