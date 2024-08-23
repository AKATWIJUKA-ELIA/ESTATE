from django.shortcuts import render

# Create your views here.


def index(request):
      return render(request, 'index.html')


def about(request):
      return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def advertise(request):
    return render(request, 'advertise.html')

def property(request):
    return render(request, 'property.html')


def news_letter(request):
    return render(request, 'news_letter.html')