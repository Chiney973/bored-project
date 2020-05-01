from django.urls import path, include
from rest_framework.routers import DefaultRouter

from activity.api_views import (
    ActivitiesViewSet,
    RandomActivityView,
    ActivityTypesView,
)
from activity.views import (
    index,
    add_activity,
)


activity_router = DefaultRouter()
activity_router.register("activities", ActivitiesViewSet)

api_urlpatterns = [
    path("", include(activity_router.urls)),
    path("activity-types/", ActivityTypesView.as_view()),
    path("random-activity", RandomActivityView.as_view(), name="random-activity")
]

urlpatterns = [
    path("", index, name="index"),
    path("add-activity", add_activity, name="add-activity")
]