from django.core.management.base import BaseCommand
from booking.models import Film, Seat
from datetime import datetime

class Command(BaseCommand):
    help = "Populate the database with initial films and seats"

    def handle(self, *args, **kwargs):
        # Add films
        films = [
            {
                "title": "Shrek",
                "description": "An ogre's adventure",
                "genre": "Animation",
                "showing_time": datetime(2025, 1, 24, 18, 0, 0),
            },
            {
                "title": "Moana",
                "description": "A sea-faring journey",
                "genre": "Adventure",
                "showing_time": datetime(2025, 1, 24, 20, 0, 0),
            },
            {
                "title": "Shark Tale",
                "description": "An underwater comedy",
                "genre": "Comedy",
                "showing_time": datetime(2025, 1, 24, 22, 0, 0),
            },
        ]

        for film_data in films:
            film, created = Film.objects.get_or_create(**film_data)
            if created:
                self.stdout.write(f"Film '{film.title}' added.")

        # Add seats (10 for each film)
        films = Film.objects.all()
        for film in films:
            for seat_number in range(1, 11):
                seat, created = Seat.objects.get_or_create(film=film, seat_number=seat_number)
                if created:
                    self.stdout.write(f"Seat {seat_number} for '{film.title}' added.")
        
        self.stdout.write("Database successfully populated.")
