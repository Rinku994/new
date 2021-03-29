from django.shortcuts import render

# Create your views here.
def home(request):
     return render(request, 'home.html')

def review(request):
     return render(request, 'review.html')

def booking(request):
     return render(request,'booking.html')