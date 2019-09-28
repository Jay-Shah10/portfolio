from django.shortcuts import render, reverse
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})