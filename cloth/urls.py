from django.urls import path
from . import views

urlpatterns = [
    path('cloths/', views.ClothListView.as_view(), name='cloths'),
    path('cloths/<int:id>/', views.ClothDetailView.as_view(), name='detail'),
    path('add-order/', views.OrderCreateView.as_view(), name='add'),
    path('male/', views.MaleClothListView.as_view(), name='male'),
    path('female/', views.FemaleClothListView.as_view(), name='female'),
    path('child/', views.ChildClothListView.as_view(), name='child'),
    path('uni/', views.UniClothListView.as_view(), name='uni'),
]