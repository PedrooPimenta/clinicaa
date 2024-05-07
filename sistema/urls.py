from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from home import views as home_views
from usuarios import views as usuarios_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', home_views.index, name='home'),
    path('consultas/', include('consultas.urls')),
    path('', include('usuarios.urls')),
]
