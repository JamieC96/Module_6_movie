from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserSignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Booking


# Sign-up View
def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserSignupForm()
    return render(request, 'booking/signup.html', {'form': form})

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)
                # Redirect to the movie listing page
                return redirect('movie_list')  # Redirect to the movie list page
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'booking/login.html', {'form': form})


# In booking/views.py

from django.shortcuts import render, get_object_or_404
from .models import Film, Seat, Booking
from django.contrib.auth.decorators import login_required

# Home page view
def home(request):
    return render(request, 'booking/home.html')


# Movie listings view
def movie_list(request):
    movies = Movie.objects.all()  # Get all the movies from the database
    return render(request, 'booking/movie_list.html', {'movies': movies})

# User Dashboard View (Displays current bookings)
@login_required
def dashboard(request):
    # Get the current user's bookings
    bookings = Booking.objects.filter(user=request.user)
    
    return render(request, 'booking/dashboard.html', {'bookings': bookings})


@login_required
def book_seat(request, film_id):
    # Get the film for which the user is booking a seat
    film = get_object_or_404(Film, id=film_id)
    
    # Get all available seats for the film (seats that are not already booked)
    available_seats = Seat.objects.filter(film=film).exclude(id__in=Booking.objects.filter(film=film).values('seat_id'))

    if request.method == "POST":
        seat_id = request.POST.get('seat_id')  # Get the selected seat ID from the form
        seat = get_object_or_404(Seat, id=seat_id)  # Get the selected seat
        
        # Check if the seat is already booked
        if Booking.objects.filter(film=film, seat=seat).exists():
            return HttpResponse("Seat already booked!", status=400)

        # Create a new booking for the user
        booking = Booking(user=request.user, film=film, seat=seat)
        booking.save()
        
        return redirect('dashboard')  # Redirect to the dashboard page after booking
    
    return render(request, 'booking/book_seat.html', {'film': film, 'available_seats': available_seats})

from django.contrib.auth.decorators import login_required

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'booking/movie_list.html', {'movies': movies})

def user_logout(request):
    """Log the user out and redirect to the login page."""
    logout(request)
    return redirect('login')  # Redirect to the login page after logging out

from .models import Film  # Import the Movie model here

def movie_list(request):
    films = Film.objects.all()  # Query the database for all films
    return render(request, 'booking/movie_list.html', {'films': films})