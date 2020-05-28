from django.shortcuts import render
from .models import ServerGroup

def index(request):
    context = {'groups': ServerGroup.objects.all()}
    return render(request, 'index.html', context)
