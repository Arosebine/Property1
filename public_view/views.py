from django.shortcuts import render, redirect
from django.http import HttpResponse 
from public_view.models import *

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
     # rent = Property.objects.filter(offer_type='Rent')[:3]
     latest = Property.objects.order_by('-created')[:3]
     sale = Property.objects.filter(offer_type='Sale')[:3]
     args = {'sale_key':sale, 'latest':latest}
     return render(request, 'public/index.html', args)

def about(request):
     team = Team.objects.order_by('-created')
     return render(request, 'public/about.html', {'team_key':team})


def detail_about(request, team_id):
     detail = Team.objects.get(id=team_id)
     return render(request, 'public/about-detail.html', {'det': detail})

def agent(request):
     return render(request, 'public/agent.html')

def rent(request):
     return render(request, 'public/rent.html')

def request(request):
     return render(request, 'public/request.html')

def property_details(request, slug, category_id):
     prop_det = Property.objects.get(slug=slug)
     related_prop = Property.objects.filter(property_type_id__id=category_id)
     return render(request, 'public/property-details.html', {'prop':prop_det, 'rel':related_prop})





def buy(request):
     return render(request, 'public/buy.html')




def register(request):
     return render(request, 'public/register.html')




def login_view(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)

         if user is not None:
             login(request, user)
             return redirect('backend:index')
         else:
             messages.error(request, 'Username and Password do not match')
     return render(request, 'public/login.html')




# def add(request):
#      return HttpResponse( 6+3 )



