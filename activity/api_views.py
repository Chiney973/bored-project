from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from activity import RandomOnEmptyQuerySetException
from activity.models import Activity
from activity.serializers import ActivitySerializer


class ActivitiesViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class RandomActivityView(APIView):

    def filter(self, request, queryset):
        type = request.query_params.get("type")
        if type:
            queryset = queryset.filter(type=type)

        participants = request.query_params.get("participants")
        if participants:
            queryset = queryset.filter(participants=participants)
        return queryset

    def get(self, request):
        queryset = self.filter(request, Activity.objects.get_queryset())
        try:
            activity = queryset.random()
        except RandomOnEmptyQuerySetException:
            raise Http404
        serializer = ActivitySerializer(activity, context={"request": request})
        return Response(serializer.data)
