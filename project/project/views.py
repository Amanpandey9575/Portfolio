from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def portfolio(request):
    return render(request,"portfolio.html")
def we_do(request):
    return render(request,"we_do.html")