from django.urls import path
from . import views
app_name='blog'
pa=path('blogpg',views.blogpg,name='blogpg')
urlpatterns=[
    pa,


]