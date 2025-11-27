from django.contrib import admin
from django.urls import path
from monday import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about),
    path('special/',views.special),
    path('fresh/',views.fresh),
    path('contact/',views.contact),
    path('blog/',views.blog),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]

