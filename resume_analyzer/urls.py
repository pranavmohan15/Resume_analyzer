from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),              # Home page
    path('analyze/', views.analyze_view, name='analyze'),  # Analyzer page
    path('register/', views.register_view, name='register'),
    path('result/<int:result_id>/', views.result_view, name='result'),
     # Authentication
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

 path(
    'logout/',
    LogoutView.as_view(next_page='home'),
    name='logout'
),

    
]