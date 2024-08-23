from django.urls import path
from . import views

urlpatterns=[
      path('',views.index,name='index'),
      path('about/',views.about, name='about'),
      path('property/',views.property, name='property'),
      path('contact/',views.contact, name='contact'),
      path('advertise/',views.advertise, name='advertise'),
      path('manageProperty/',views.manageProperty, name='manageProperty'),
      path('newsletter/', views.news_letter,name="news_letter"),
]