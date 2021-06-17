from django.urls import path
#from . import views
from .views import AddPostView, HomeView, BlogDeetView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,LikeView,AddCommentView

urlpatterns = [
    #path('',views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',BlogDeetView.as_view(),name="BlogDeets"),
    path('add_post/',AddPostView.as_view(),name="Add_Post"),
    path('add_category/',AddCategoryView.as_view(),name="Add_Category"),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name="Edit_Post"),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name="Delete_Post"),
    path('category/<str:cats>/',CategoryView,name="category"),
    path('like/<int:pk>',LikeView,name="like_post"),
    path('article/<int:pk>/add_comment',AddCommentView.as_view(),name="Add_Comment"),
]