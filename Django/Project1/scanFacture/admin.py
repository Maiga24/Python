from django.contrib import admin
from .models import Facture, LigneArticle

class LigneArticleInline(admin.TabularInline):
    model = LigneArticle
    extra = 1

class FactureAdmin(admin.ModelAdmin):
    inlines = [LigneArticleInline]
    list_display = ['fournisseur', 'numero_facture', 'date_facture', 'montant_ttc']

admin.site.register(Facture, FactureAdmin)
