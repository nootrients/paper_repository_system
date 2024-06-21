from django.core.management.base import BaseCommand
from colleges.models import UniversityBranch, RegionalGroup


class Command(BaseCommand):
    help = "Inserts a list of values or instances for `UniversityBranch` table."

    def handle(self, *args, **options):
        # Fetch existing RegionalGroup instances
        try:
            metro_manila = RegionalGroup.objects.get(region_name="Metro Manila")
            central_luzon = RegionalGroup.objects.get(region_name="Central Luzon")
            south_luzon = RegionalGroup.objects.get(region_name="South Luzon")
        except RegionalGroup.DoesNotExist as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
            return

        # Create instances
        # Branch and Campuses within Metro Manila
        UniversityBranch.objects.create(
            branch_name="PUP Sta. Mesa, Manila", regional_group=metro_manila
        )
        UniversityBranch.objects.create(
            branch_name="PUP Taguig", regional_group=metro_manila
        )
        UniversityBranch.objects.create(
            branch_name="PUP Quezon", regional_group=metro_manila
        )
        UniversityBranch.objects.create(
            branch_name="PUP San Juan", regional_group=metro_manila
        )

        # Branch and Campuses within Central Luzon
        UniversityBranch.objects.create(
            branch_name="PUP Bataan", regional_group=central_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Sta. Maria, Bulacan", regional_group=central_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Pulilan, Bulacan", regional_group=central_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Cabiao, Nueva Ecija", regional_group=central_luzon
        )

        # Branch and Capuses within South Luzon
        UniversityBranch.objects.create(
            branch_name="PUP Lopez, Quezon", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Mulanay, Quezon", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP General Luna, Quezon", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Unisan, Quezon", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Ragay, Camarines Sur", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Maragondon, Cavite", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Alfonso, Cavite", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Bansud, Oriental Mindoro", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Sablayan, Occidental Mindoro", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Binan, Laguna", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP San Pedro, Laguna", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Sta. Rosa, Laguna", regional_group=south_luzon
        )
        UniversityBranch.objects.create(
            branch_name="PUP Calauan, Laguna", regional_group=south_luzon
        )

        self.stdout.write(
            self.style.SUCCESS("Successfully added UniversityBranch records")
        )
