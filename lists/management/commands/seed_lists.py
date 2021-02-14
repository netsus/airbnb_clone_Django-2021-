import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

NAME = "lists"


class Command(BaseCommand):

    help = f"This command creates {NAME}"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {NAME} do you want to create",
        )

    def handle(self, *args, **options):

        number = int(options.get("number"))
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),  # ForeignKey 추가
            },
        )
        created_lists = seeder.execute()
        cleaned = flatten(created_lists.values())
        for pk in cleaned:
            list_object = list_models.List.objects.get(pk=pk)
            to_add = [random.choice(rooms) for i in range(0, random.randint(5, 30))]
            list_object.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME} created!"))