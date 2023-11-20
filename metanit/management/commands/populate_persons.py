from django.core.management.base import BaseCommand
from metanit.models import Person 

class Command(BaseCommand):
    help = 'Populates the metanit_person table in PostgreSQL'

    def handle(self, *args, **options):
        persons_data = [
            {'id': 1, 'name': 'John', 'age': 25},
            {'id': 2, 'name': 'Jane', 'age': 30},
        ]

        for data in persons_data:
            Person.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated metanit_person table'))

