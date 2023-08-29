from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Details

def home(request):
    data = Details.objects.all()
    count = data.count()
    return render(request, 'landing.html',{"count":count})

