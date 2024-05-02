from django.db import models


class Categorie(models.Model):
    nomCat = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.nomCat} - {self.description}"
    
    def produitPresent(self):
        return self.produit_set.exists()


class Produit(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.TextField()
    prix = models.IntegerField(default=500)
    quantite_disponible = models.IntegerField(default=1)
    catId = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='produit_set')
    
    def __str__(self):
        return f"{self.libelle} - {self.description} - {self.prix} - {self.categorie} - {self.quantite_disponible}"

    def delete_produit(self):
        self.delete()


class Vente(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    produit = models.ManyToManyField(
        Produit, through='ProduitVendu', through_fields=('vente', 'produit'))


class ProduitVendu(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(default=1)
    prix_unitaire = models.IntegerField(default=0)


class Transaction(models.Model):
    numero = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    montant = models.FloatField(default=1000)
    service = models.CharField(max_length=10, blank=True, null=True)
    type_transaction = models.CharField(max_length=10, blank=True, null=True)
