from django.core.management.base import BaseCommand
from colleges.models import UniversityBranch


class Command(BaseCommand):
    help = "Inserts a list of values or instances for `UniversityBranch` table."

    def handle(self, *args, **options):

        # Branch and Campuses within Metro Manila
        UniversityBranch.objects.create(
            branch_name="PUP Sta. Mesa, Manila", regional_group=1
        )
        UniversityBranch.objects.create(branch_name="PUP Taguig", regional_group=1)
        UniversityBranch.objects.create(branch_name="PUP Quezon", regional_group=1)
        UniversityBranch.objects.create(branch_name="PUP San Juan", regional_group=1)

        # Branch and Campuses within Central Luzon
        UniversityBranch.objects.create(branch_name="PUP Bataan", regional_group=2)
        UniversityBranch.objects.create(
            branch_name="PUP Sta. Maria, Bulacan", regional_group=2
        )
        UniversityBranch.objects.create(
            branch_name="PUP Pulilan, Bulacan", regional_group=2
        )
        UniversityBranch.objects.create(
            branch_name="PUP Cabiao, Nueva Ecija", regional_group=2
        )

        # Branch and Capuses within South Luzon
        UniversityBranch.objects.create(
            branch_name="PUP Lopez, Quezon", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Mulanay, Quezon", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP General Luna, Quezon", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Unisan, Quezon", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Ragay, Camarines Sur", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Maragondon, Cavite", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Alfonso, Cavite", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Bansud, Oriental Mindoro", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Sablayan, Occidental Mindoro", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Binan, Laguna", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP San Pedro, Laguna", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Sta. Rosa, Laguna", regional_group=3
        )
        UniversityBranch.objects.create(
            branch_name="PUP Calauan, Laguna", regional_group=3
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully added UniversityBranch records")
        )
