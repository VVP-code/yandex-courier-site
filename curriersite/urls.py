from django.urls import path
from . import views
urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('benefits/', views.Benefits.as_view(), name='benefits'),
    path('requirements/', views.Requirements.as_view(), name='requirements'),
    path('FAQ/', views.FAQ.as_view(), name='FAQ'),
]