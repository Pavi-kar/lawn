from django.urls import path
from . import views
app_name='contact'
pa=path('contactpg',views.contactpg,name='contactpg')
urlpatterns=[
    pa,


]