
from app import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('hot/', views.hot, name='hot'),
    path('admin/', admin.site.urls),
    path('ask/', views.ask, name='ask'),
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('login/', views.login, name='login'),
    path('register', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
]