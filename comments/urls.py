from django.urls import path
from comments import views

urlpatterns = [
    path('comments/', views.PostList.as_view()),
]