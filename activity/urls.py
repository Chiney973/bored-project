from django.urls import path, include
from rest_framework.routers import DefaultRouter

from activity.api_views import (
    ActivitiesViewSet,
    RandomActivityView,
)


activity_router = DefaultRouter()
activity_router.register("activities", ActivitiesViewSet)

urlpatterns = [
    path("", include(activity_router.urls)),
    path("random-activity", RandomActivityView.as_view(), name="random-activity")
]