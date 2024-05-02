
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from back_end.models import Livre
# Create your views here.



def parent (request):
    return render(request, 'parent.html')

def accueil (request):
   roman = Livre.objects.all()
   return render (request, 'accueil.html',{"livres":roman})

def services (request):
    return render(request, 'services.html')

def contact (request):
    return render(request, 'contact.html')

def enregistrerUnLivre(request):
   if request.method == "GET":
      return render(request, "nouveauLivre.html")
   else:
      titre = request.POST['titre']
      auteur = request.POST['auteur']
      description = request.POST['description']
      prix = request.POST['prix']
      Livre.objects.create(titre=titre,auteur=auteur,description=description,prix=prix)
      return redirect('front_end:accueil')