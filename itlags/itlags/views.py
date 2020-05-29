from django.shortcuts import render
from .models import ServerGroup
from ipware import get_client_ip


def index(request):
    client_ip, is_routable = get_client_ip(request)

    context = {'groups': ServerGroup.objects.all(),
               'client_ip': client_ip,
               'is_routable': is_routable}
    return render(request, 'index.html', context)


def reports(request):
    context = {}
    return render(request, 'reports.html', context)
