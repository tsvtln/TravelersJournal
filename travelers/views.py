from travelers.forms import TravelerForm, TripForm
from travelers.models import Trip, Traveler
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    traveler_exists = Traveler.objects.exists()
    return render(request, 'index.html', {'traveler_exists': traveler_exists})


def create_traveler(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TravelerForm()
    return render(request, 'create-traveler.html', {'form': form})


def all_trips(request):
    trips = Trip.objects.all().order_by('-start_date')
    traveler_exists = Traveler.objects.exists()
    return render(request, 'all-trips.html', {
        'trips': trips,
        'traveler_exists': traveler_exists,
    })


def create_trip(request):
    if not Traveler.objects.exists():
        return redirect('create_traveler')

    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.traveler = Traveler.objects.first()
            trip.save()
            return redirect('all_trips')
    else:
        form = TripForm()

    traveler_exists = Traveler.objects.exists()

    return render(request, 'create-trip.html', {'form': form, 'traveler_exists': traveler_exists})


def trip_details(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    traveler_exists = Traveler.objects.exists()
    return render(request, 'details-trip.html', {'trip': trip, 'traveler_exists': traveler_exists})


def edit_trip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TripForm(instance=trip)

    traveler_exists = Traveler.objects.exists()

    return render(request, 'edit-trip.html', {'form': form, 'traveler_exists': traveler_exists})


def delete_trip(request, trip_pk):
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        trip.delete()
        return redirect('all_trips')

    traveler_exists = Traveler.objects.exists()

    return render(request, 'delete-trip.html', {'trip': trip, 'traveler_exists': traveler_exists})


def traveler_details(request):
    traveler = Traveler.objects.first()
    if not traveler:
        return redirect('create_traveler')

    trips = traveler.ordered_trips()
    traveler_exists = Traveler.objects.exists()

    return render(request, 'details-traveler.html', {
        'traveler': traveler,
        'trips': trips,
        'has_trips': trips.exists(),
        'traveler_exists': traveler_exists,
    })


def edit_traveler(request):
    traveler = Traveler.objects.first()
    if not traveler:
        return redirect('create_traveler')

    if request.method == 'POST':
        form = TravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('traveler_details')
    else:
        form = TravelerForm(instance=traveler)

    traveler_exists = Traveler.objects.exists()

    return render(request, 'edit-traveler.html', {'form': form, 'traveler_exists': traveler_exists})


def delete_traveler(request):
    traveler = Traveler.objects.first()

    if not traveler:
        return redirect('index')

    if request.method == 'POST':
        traveler.delete()
        return redirect('index')

    traveler_exists = Traveler.objects.exists()

    return render(request, 'delete-traveler.html', {
        'traveler': traveler,
        'traveler_exists': traveler_exists
    })
