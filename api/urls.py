from django.urls import path
from . import views


urlpatterns = [
    path('fillup/', views.ProfileView.as_view(), name = 'fillup'),
    path('showup/', views.ProfileView.as_view(), name = 'showup')
]
