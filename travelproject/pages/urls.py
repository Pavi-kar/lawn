from django.urls import path
from . import views
app_name='pages'

urlpatterns=[
    path('faq', views.faq, name='faq'),
    path('pricing', views.pricing, name='pricing'),
]