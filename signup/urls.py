from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'signup'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name="signup/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="signup:index"), name='logout'),
]