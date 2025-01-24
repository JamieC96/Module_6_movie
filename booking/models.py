from django.db import models
from django.contrib.auth.models import User

# Film Model
class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    showing_time = models.DateTimeField()

    def __str__(self):
        return self.title

# Seat Model
class Seat(models.Model):
    seat_number = models.IntegerField()
    is_booked = models.BooleanField(default=False)
    film = models.ForeignKey(Film, related_name='seats', on_delete=models.CASCADE)

    def __str__(self):
        return f"Seat {self.seat_number} for {self.film.title}"
    
    @classmethod
    
    def create_seats_for_film(cls, film, number_of_seats=10):
        for seat_number in range(1, number_of_seats + 1):
            cls.objects.create(film=film, seat_number=seat_number)

# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.user.username} for {self.film.title} - Seat {self.seat.seat_number}"
    

