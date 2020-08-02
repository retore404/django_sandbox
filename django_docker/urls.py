from django.contrib import admin
from django.urls import include, path
from django.views.generic import base

urlpatterns = [
    path('signup/', include('signup.urls')),
    path('admin/', admin.site.urls),
    path('accounts/login/', base.RedirectView.as_view(pattern_name="signup:login")),
    path('accounts/profile/', base.RedirectView.as_view(pattern_name="signup:index")),
]