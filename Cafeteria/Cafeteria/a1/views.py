from django.shortcuts import render

def cafe(request):
    return render(request, 'a1/index.html', {})