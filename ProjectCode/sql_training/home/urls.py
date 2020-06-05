from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views as user_views
# from .views import FilteredSqlProblemListView

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
]