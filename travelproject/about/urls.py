from django.urls import path
from . import views
app_name='about'
pa=path('aboutpg',views.aboutpg,name='aboutpg')
urlpatterns=[
    pa,


]