from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),  # Serve o app Dash
]
