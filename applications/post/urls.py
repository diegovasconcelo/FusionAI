from django.urls import path
from . import views

app_name = 'post_app'

urlpatterns = [
    path('post-list/',views.ArticleList.as_view(),name='list'),
    path('post-detail/<pk>/',views.ArticleDetailView.as_view(),name='detail')
]