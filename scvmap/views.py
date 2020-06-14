from django.shortcuts import render


def map_(request):
    return render(request, 'map/navermap.html')