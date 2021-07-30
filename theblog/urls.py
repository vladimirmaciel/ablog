from django.urls import path
# from .import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletPostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    # path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/<int:pk>/remove', DeletPostView.as_view(), name='delete-post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
]
