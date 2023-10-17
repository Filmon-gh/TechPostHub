from django.urls import path
from profiles import views

urlpatterns = [
    path('profiles/', views.CustomProfileListView.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
]