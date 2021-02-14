from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "I love you"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How much I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
            self.stdout.write(self.style.WARNING("I love you"))
            self.stdout.write(self.style.ERROR("I love you"))
