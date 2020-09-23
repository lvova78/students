from django.http import HttpResponse
from django.shortcuts import render

def journal(request):
    return render(request, 'students/journal.html')