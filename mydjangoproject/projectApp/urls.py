from django.urls import path

from . import views

urlpatterns = [
    path('createdummy/createpost/', views.Index),
    path('createdummy/createcomment/', views.IndexComment),
    path('posts', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/<int:pk>/comments', views.CommentsEach.as_view()),
    path('comments/', views.CommentsList.as_view()),
    path('comments/<int:pk>/', views.CommentsDetail.as_view()),
]