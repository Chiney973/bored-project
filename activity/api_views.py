from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from activity import RandomOnEmptyQuerySetException
from activity.models import Activity
from activity.serializers import (
    ActivitySerializer,
    ActivityTypeSerializer,
)


class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class RandomActivityView(APIView):

    def filter(self, request, queryset):
        _type = request.query_params.get("type")
        if _type:
            queryset = queryset.filter(type=_type)

        participants = request.query_params.get("participants")
        if participants:
            queryset = queryset.filter(participants=participants)

        price = request.query_params.get("price")
        if price:
            queryset = queryset.filter(price=price)
        
        return queryset

    def get(self, request):
        queryset = self.filter(request, Activity.objects.get_queryset())
        try:
            activity = queryset.random()
        except RandomOnEmptyQuerySetException:
            raise Http404
        serializer = ActivitySerializer(activity, context={"request": request})
        return Response(serializer.data)


class ActivityTypesView(ListAPIView):
    # Activity.objects.all().distinct("type") if use of postgresql
    queryset = Activity.objects.values("type").distinct()
    serializer_class = ActivityTypeSerializer
    pagination_class = None
