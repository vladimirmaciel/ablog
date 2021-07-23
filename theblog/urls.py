from django.urls import path
# from .import views
from .views import  HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletPostView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/<int:pk>/remove', DeletPostView.as_view(), name='delete-post')
]