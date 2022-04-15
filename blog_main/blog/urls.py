from django.urls import path
from . import views

# 해당 App내부에서 url 패턴들
urlpatterns = [
    # Class-based views(장고에서 제공하는 것)
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.show_category_posts),
    path('tag/<str:slug>/',views.show_tag_posts),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view())

    # Function view(직접 제작)
    # path('', views.index),
    # path('<int:pk>/', views.single_post_page),
]
