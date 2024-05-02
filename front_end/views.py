
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from back_end.models import *


def accueil(request):
    produit = Produit.objects.all()
    return render(request, 'accueil.html', {"produits": produit})

def categorie(request):
    categorie = Categorie.objects.all()
    return render(request, 'categorie.html', {"categories": categorie})

def vente(request):
    produit = Produit.objects.all()
    return render(request, 'vente.html', {"produits": produit})


def dashBord(request):
    return render(request, 'dashBord.html')

def creerCategorie(request):
    if request.method == 'GET':
        return render(request, 'creerCategorie.html')
    else:
        nomCat = request.POST['nomCat']
        description = request.POST['description']

        Categorie.objects.create(nomCat=nomCat, description=description)


        return redirect('front_end:categorie')
    
def creerProduit(request):
    if request.method == "GET":
        categories = Categorie.objects.all()
        return render(request, "nouveauProduit.html", {"categories": categories})
    else:
        libelle = request.POST['libelle']
        catId = request.POST['catId']
        description = request.POST['description']
        quantite_disponible = request.POST['quantite_disponible']
        prix = request.POST['prix']
        oCat = Categorie.objects.get(pk=request.POST['catId'])

        # Créer le produit en associant la catégorie
        Produit.objects.create(libelle=libelle, description=description, prix=prix,
                               quantite_disponible=quantite_disponible, catId=oCat)
        return redirect('front_end:accueil')


def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    produit.delete()
    return redirect('front_end:accueil')

def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)

    if request.method == 'POST':
        if not categorie.produitPresent():
            categorie.delete()
            return redirect('front_end:categorie')
        else:
            message="Impossible de supprimer cette catégorie. Des produits sont associés à cette catégorie."
            return render(request, 'categorie.html', {'message': message})

    return render(request, 'categorie.html', {'categorie': categorie})



def mettre_a_jour_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    categories = Categorie.objects.all()

    if request.method == 'GET':
        return render(request, 'mettre_a_jour_produit.html', {'produit': produit, 'categories': categories})

    elif request.method == 'POST':
        libelle = request.POST['libelle']
        categorie_id = request.POST['categorie'] 
        quantite_disponible = request.POST['quantite_disponible']
        description = request.POST['description']
        prix = request.POST['prix']

        categorie = get_object_or_404(Categorie, pk=categorie_id)

        produit.libelle = libelle
        produit.categorie = categorie
        produit.quantite_disponible = quantite_disponible
        produit.description = description
        produit.prix = prix

        produit.save()

        return redirect('front_end:accueil')

def modifier_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)

    if request.method == 'GET':
        return render(request, 'modifier_categorie.html', {'categorie': categorie})
    elif request.method == 'POST':
        nomCat = request.POST['nomCat']
        description = request.POST['description']

        categorie.nomCat = nomCat
        categorie.description = description

        categorie.save()

        return redirect('front_end:categorie')


def rechercher_article(request):
    query = request.GET.get('q', '')

    if query:
        articles = Produit.objects.filter(libelle__icontains=query)
    else:
        articles = Produit.objects.all()

    return render(request, 'recherche_article.html', {'articles': articles, 'query': query})

def rechercher_categorie(request):
    query = request.GET.get('q', '')

    if query:
        categories = Categorie.objects.filter(nomCat__icontains=query)
    else:
        categories = Categorie.objects.all()

    return render(request, 'recherche_categorie.html', {'categories': categories, 'query': query})


       

def recherche_article_vente(request):
    # Récupérer la requête de recherche depuis les paramètres GET
    query = request.GET.get('q', '')

    if query:
        # Rechercher les articles par libellé (insensible à la casse)
        articles = Produit.objects.filter(libelle__icontains=query)
    else:
        # Si aucune requête n'est spécifiée, récupérer tous les articles
        articles = Produit.objects.all()

    return render(request, 'recherche_article_vente.html', {'articles': articles, 'query': query})


def valide_vente(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    quantite_vendue = int(request.POST['quantite_disponible'])

    if quantite_vendue <= produit.quantite_disponible:
        # Créer une vente
        vente = Vente.objects.create()

        # Ajouter le produit vendu à la vente
        produit_vendu = ProduitVendu.objects.create(
            vente=vente,
            produit=produit,
            quantite=quantite_vendue,
            prix_unitaire=produit.prix
        )

        # Mettre à jour la quantité disponible du produit
        produit.quantite_disponible -= quantite_vendue
        produit.save()

        # Remplacez 'nom_de_la_vue' par le nom de la vue que vous souhaitez rediriger après la vente
        return redirect('front_end:dashBord')

    else:
        return render(request, 'erreur_quantite.html')


def flooz(request):
    return render(request, 'flooz.html')


def tmoney(request):
    return render(request, 'tmoney.html')


def envoie_flooz(request):
    return render(request, "envoie_flooz.html")


def retrait_flooz(request):
    return render(request, "retrait_flooz.html")


def envoie_tmoney(request):
    return render(request, "envoie_tmoney.html")


def retrait_tmoney(request):
    return render(request, "retrait_tmoney.html")


def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "transactions.html", {"transactions": transactions})


def transaction(request):
    if request.method == 'POST':
        numero = request.POST['numero']
        montant = request.POST['montant']
        service = request.POST['service']
        type_transaction = request.POST['type_transaction']

        # Créez une nouvelle instance de Transaction
        Transaction.objects.create(
            numero=numero, montant=montant, service=service, type_transaction=type_transaction)

        return redirect('front_end:dashBord')

    return render(request, 'envoie.html')


def operation_vente(request):
    produits = Produit.objects.all()
    vente = Vente.objects.all()
    produits_vendus = ProduitVendu.objects.all()

    # Utilisez une liste pour stocker les produits vendus avec leurs totaux
    produits_total = []

    for produit_vendu in produits_vendus:
        total = produit_vendu.prix_unitaire * produit_vendu.quantite
        # Ajoutez le produit vendu avec son total à la liste
        produits_total.append({"produit_vendu": produit_vendu, "total": total})

    # Passez les produits vendus avec leurs totaux au modèle
    return render(request, 'operation_vente.html', {"produits": produits, "produits_totals": produits_total, "vente": vente})
