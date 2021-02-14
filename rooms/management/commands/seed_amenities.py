from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    """
    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How much I love you?",
        )
    """

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Beachfront",
            "Breakfast",
            "Carbon monoxide alarm",
            "Crib",
            "Dedicated workspace",
            "Dryer",
            "Hair dryer",
            "Hangers",
            "Heating",
            "High chair",
            "Indoor fireplace",
            "Iron",
            "Kitchen",
            "Piano",
            "Private bathroom",
            "Self check-in",
            "Shampoo",
            "Smoke alarm",
            "TV",
            "Washer",
            "Waterfront",
            "Wifi",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
