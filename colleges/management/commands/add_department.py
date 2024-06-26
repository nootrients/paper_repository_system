from django.core.management.base import BaseCommand
from colleges.models import Department


class Command(BaseCommand):
    help = "Inserts a list of values or instances for `Department` table."

    def handle(self, *args, **options):
        Department.objects.create(name="College of Accountancy and Finance")
        Department.objects.create(name="College of Arts and Letters")
        Department.objects.create(
            name="College of Architecture, Design and the Built Environment"
        )
        Department.objects.create(name="College of Business Administration")
        Department.objects.create(name="College of Computer and Information Sciences")
        Department.objects.create(name="College of Communication")
        Department.objects.create(name="College of Education")
        Department.objects.create(name="College of Engineering")
        Department.objects.create(name="College of Human Kinetics")
        Department.objects.create(
            name="College of Political Science and Public Administration"
        )
        Department.objects.create(name="College of Science")
        Department.objects.create(name="College of Social Sciences and Development")
        Department.objects.create(
            name="College of Tourism, Hospitality and Transportation Management"
        )
        Department.objects.create(name="Open University System")
        Department.objects.create(name="Institute of Technology")

        self.stdout.write(self.style.SUCCESS("Successfully added Department records"))
