from multiprocessing import context
from django.shortcuts import render
from .forms import ReservationForm

# Create your views here.
def reserve(request):
    reserve_form = ReservationForm()
    if request.method == "POST":
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        reserve_form = ReservationForm()   
    context = {
        "reserve_form":reserve_form,
        }
    return render(request,"reservation/reservation.html",context)
