from django.db import models
from django.contrib.auth.models import User

class Facture(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    fournisseur = models.CharField(max_length=255)
    numero_facture = models.CharField(max_length=100)
    date_facture = models.DateField()
    montant_ht = models.DecimalField(max_digits=10, decimal_places=2)
    tva = models.DecimalField(max_digits=10, decimal_places=2)
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=2)
    fichier = models.FileField(upload_to='factures/')

    def __str__(self):
        return f"{self.fournisseur} - {self.numero_facture}"

class LigneArticle(models.Model):
    facture = models.ForeignKey(Facture, related_name='articles', on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    quantite = models.PositiveIntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.designation} x{self.quantite}"
