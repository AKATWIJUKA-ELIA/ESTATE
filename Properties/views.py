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
                  
def manageProperty(request):
    return render(request, 'manageProperty.html')

def property(request):
    return render(request, 'property.html')


def news_letter(request):
    return render(request, 'news_letter.html')


def Advertise(request):
      if request.method == 'POST':
            property_type = request.POST['property_type']
            number_of_rooms = request.POST['number_of_rooms']
            location = request.POST['location']
            price = request.POST['price']
            description = request.POST['description']
      return render(request, 'Advertise.html')      
            
def sign_in(request):
      return render(request,"sign-in.html")

def sign_up(request):
      return render(request,"sign-up.html")             