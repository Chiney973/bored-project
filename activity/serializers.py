from rest_framework import serializers

from activity.models import Activity


class ActivitySerializer(serializers.HyperlinkedModelSerializer):

    key = serializers.CharField(source="id", read_only=True)
    activity = serializers.CharField(source="description")

    class Meta:
        model = Activity
        fields = (
            "url",
            "activity",
            "accessibility",
            "type",
            "participants",
            "price",
            "link",
            "key",
        )
