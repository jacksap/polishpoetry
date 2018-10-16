from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learn/', views.learn, name='learn'),
    path('login/', views.login_view, name="login"),
    path('poets/', views.poets_index, name='poets_index'),
    path('poems/', views.poems_index, name='poems_index'),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('poets/<int:poet_id>/', views.poets_detail, name='poets_detail'),
    path('poems/<int:poem_id>/', views.poems_detail, name='poems_detail'),
    path('poets/create/', views.PoetCreate.as_view(), name='poets_create'),
    path('poets/<int:pk>/update/', views.PoetUpdate.as_view(), name='poets_update'),
    path('poets/<int:pk>/delete/', views.PoetDelete.as_view(), name='poets_delete'),
    path('poems/create/', views.PoemCreate.as_view(), name='poems_create'),
    path('poems/<int:pk>/update/', views.PoemUpdate.as_view(), name='poems_update'),
    path('poems/<int:pk>/delete/', views.PoemDelete.as_view(), name='poems_delete'),
    path('poems/<int:poem_id>/add_comment/', views.add_comment, name='add_comment'),
    path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comment_delete'),
    path('collections/', views.collections_index, name='collections_index'),
    path('collections/<int:collection_id>/', views.collections_detail, name='collections_detail'),
    path('collections/create/', views.CollectionCreate.as_view(), name='collections_create'),
    path('collections/<int:pk>/update/', views.CollectionUpdate.as_view(), name='collections_update'),
    path('collections/<int:pk>/delete/', views.CollectionDelete.as_view(), name='collections_delete'),
]