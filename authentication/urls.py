from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import login_forms, authentication, logout_account

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', login_forms, name='auth_login'),
    path('authLogin/', authentication , name='auth_process_login'),
    path('authLogout/', logout_account , name='auth_process_logout'),
]
