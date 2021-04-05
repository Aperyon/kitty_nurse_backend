"""kitty_nurse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as drf_views
from rest_framework.routers import DefaultRouter

import pets.views
import events.views
import users.views


router = DefaultRouter()
router.register("pets", pets.views.PetViewSet, basename="pet")
router.register("events", events.views.EventViewSet, basename="event")
router.register("event-types", events.views.EventTypeViewSet, basename="eventtype")


api_urlpatterns = [
    path("", include(router.urls)),
    path("signup/", users.views.signup_user_view, name="signup"),
    path("login/", drf_views.obtain_auth_token, name="login"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
