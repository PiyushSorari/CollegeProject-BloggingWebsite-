from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('', views.home, name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"), #pk is the primary key of each blog entry
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/edit/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
]


urlpatterns += staticfiles_urlpatterns()
