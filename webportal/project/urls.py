from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('layout/', views.layout, name='layout'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('interactive_resume/', views.interactive_resume, name='interactive_resume'),
    path('snake_game/', views.snake_game, name='snake_game'),
]
