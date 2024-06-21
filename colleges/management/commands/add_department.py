from django.core.management.base import BaseCommand
from colleges.models import Department


class Command(BaseCommand):
    help = "Inserts a list of values or instances for `Department` table."

    def handle(self, *args, **options):
        Department.objects.create(department_name="Computer Science")

        self.stdout.write(self.style.SUCCESS("Successfully added Department records"))
