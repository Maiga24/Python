from django.urls import path
from . import views

urlpatterns = [
    path('ajouter/', views.ajouter_facture, name='ajouter_facture'),
    path('liste/', views.liste_factures, name='liste_factures'),
    path('detail/<int:facture_id>/', views.detail_facture, name='detail_facture'),
    path('modifier/<int:facture_id>/', views.modifier_facture, name='modifier_facture'),
    path('supprimer/<int:facture_id>/', views.supprimer_facture, name='supprimer_facture'),
]
