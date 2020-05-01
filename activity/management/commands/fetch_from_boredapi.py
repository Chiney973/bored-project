import requests
from django.core.management.base import BaseCommand

from activity.models import Activity

BORED_API_ENDPOINT = "https://www.boredapi.com/api/activity"


class Command(BaseCommand):
    help = "Fetching activities from boredapi to fill our database"

    def add_arguments(self, parser):
        parser.add_argument("amount", type=int)

    def handle(self, *args, **options):
        for _i in range(options["amount"]):
            response = requests.get(BORED_API_ENDPOINT)
            json = response.json()
            json["price"] = 0 if json["price"] == "" else json["price"]
            json["accessibility"] = 0 if json["accessibility"] == "" else json["accessibility"]
            Activity.objects.get_or_create(
                id=json["key"],
                description=json["activity"],
                accessibility=json["accessibility"],
                type=json["type"],
                participants=json["participants"],
                price=json["price"],
                link=json["link"],
            )
