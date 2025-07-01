from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.registration, name="register" ),
    path('dashboard/', views.dash_board_view, name="dashboard"),
    path('updateSTU/', views.updateSTUinfo, name="updateSTU"),
]


from django.urls import path
from . import views

#urlpatterns = [
    #path('', views.home_view, name='home'),
    #path('info', views.info_view, name='info'),

#]