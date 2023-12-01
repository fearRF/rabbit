from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rabbit.views import login_after_reset_password


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rabbit.urls")),
    path("accounts/password/reset/key/done/", login_after_reset_password, name="account_reset_password_from_key_done"),
    path("accounts/", include("allauth.urls")),
]
