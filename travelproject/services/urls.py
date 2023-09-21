from django.urls import path
from . import views
app_name='services'
pa=path('servicespg',views.servicespg,name='servicespg')
urlpatterns=[
    pa,


]