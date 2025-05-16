from django.shortcuts import render
import datetime

# Create your views here.
def index(request, simulate=0):
    now = datetime.datetime.now()
    return render(request, 'isThisNewYear/newyear.html', {
        "newyear": (now.month == 1 and now.day == 1) or bool(simulate),
        "today": now,
        "simulate": bool(simulate),
    })