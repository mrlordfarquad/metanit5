from django.core.management.base import BaseCommand
from metanit.models import Game

class Command(BaseCommand):
    help = 'Populates the metanit_game table in PostgreSQL'

    def handle(self, *args, **options):
        games_data = [
            {'game_id': 1, 'title': 'chess', 'content': 'chess', 'pub_date': '2023-11-19', 'file': 'chess.html'},
            {'game_id': 2, 'title': 'tetris', 'content': 'tetris', 'pub_date': '2023-11-19', 'file': 'tetris.html'},
        ]

        for data in games_data:
            Game.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated metanit_game table'))

