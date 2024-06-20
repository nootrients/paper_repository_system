from django.core.management.base import BaseCommand
from colleges.models import RegionalGroup


class Command(BaseCommand):
    help = "Inserts a list of values or instances for `RegionalGroup` table."

    def handle(self, *args, **options):
        RegionalGroup.objects.create(region_name="Metro Manila")
        RegionalGroup.objects.create(region_name="Central Luzon")
        RegionalGroup.objects.create(region_name="South Luzon")

        self.stdout.write(
            self.style.SUCCESS("Successfully added RegionalGroup records")
        )
