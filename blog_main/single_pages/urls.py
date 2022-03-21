from django.urls import path
from . import views

# 해당 앱내부에서 사용할 url패턴들
urlpatterns = [
    path('', views.landing),
    path('about_me/', views.about_me),
]