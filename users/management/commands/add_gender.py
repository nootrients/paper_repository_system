from django.core.management.base import BaseCommand
from models import Gender


class Command(BaseCommand):
    help = "Inserts a list of values or instances for `Gender` table."

    def handle(self, *args, **options):
        Gender.objects.create(gender_name="Male")
        Gender.objects.create(gender_name="Female")
        Gender.objects.create(gender_name="Prefer not to say")

        self.stdout.write(self.style.SUCCESS("Successfully added Gender records"))
