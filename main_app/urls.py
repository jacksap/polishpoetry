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
]