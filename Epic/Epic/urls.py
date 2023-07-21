"""
URL configuration for Epic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView
)

from rest_framework import routers

from crm.views import (
    ContractViewSet,
    ClientViewSet,
    EventViewSet
)


def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.SimpleRouter()
router.register(_('contract'), ContractViewSet, basename='contract')
router.register(_('client'), ClientViewSet, basename='client')
router.register(_('event'), EventViewSet, basename='event')


urlpatterns = [
    path('crm/', include(router.urls)),
    path(
        "admin/password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="admin_password_reset",
    ),
    path(
        "admin/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("admin/", admin.site.urls, name="admin"),
    # YOUR PATTERNS
    path('crm/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('crm/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('crm/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # simplejwt urls and views for the Swagger
    path('crm/login/', TokenObtainPairView.as_view(), name='login'),
    path('crm/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('crm/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('crm/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('crm/token/black_list/', TokenBlacklistView.as_view(), name='token_black_list'),
    path('sentry-debug/', trigger_error),
]
