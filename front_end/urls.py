
from django.urls import path
from . import views

app_name = 'front_end'

urlpatterns = [
    path('nouveauProduit/', views.creerProduit, name='nouveauProduit'),
    path('creerCategorie/', views.creerCategorie, name='creerCategorie'),
    path('accueil/', views.accueil, name='accueil'),
    path('categorie/', views.categorie, name='categorie'),
    path('vente/', views.vente, name='vente'),
    path('valide_vente/<int:produit_id>/', views.valide_vente, name='valide_vente'),
    path('dashBord', views.dashBord, name='dashBord'),
    path('rechercher', views.rechercher_article, name='rechercher_article'),
    path('recherche_article_vente', views.recherche_article_vente, name='recherche_article_vente'),
    path('rechercher_categorie', views.rechercher_categorie, name='rechercher_categorie'),
    path('supprimer_produit/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('supprimer_categorie/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('mettre_a_jour_produit/<int:produit_id>/', views.mettre_a_jour_produit, name='mettre_a_jour_produit'),
    path('modifier_categorie/<int:categorie_id>/', views.modifier_categorie, name='modifier_categorie'),
    path('flooz', views.flooz, name='flooz'),
    path('tmoney', views.tmoney, name='tmoney'),
    path('envoie_flooz', views.envoie_flooz, name='envoie_flooz'),
    path('retrait_flooz', views.retrait_flooz, name='retrait_flooz'),
    path('envoie_tmoney', views.envoie_tmoney, name='envoie_tmoney'),
    path('retrait_tmoney', views.retrait_tmoney, name='retrait_tmoney'),
    path('transaction', views.transaction, name='transaction'),
    path('transactions', views.transactions, name='transactions'),
    path('operation_de_vente', views.operation_vente, name='operation_vente'),
]