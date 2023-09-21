from django.urls import path
from . import views
app_name='portfolio'
pa=path('portfoliopg',views.portfoliopg,name='portfoliopg')
urlpatterns=[
    pa,
]