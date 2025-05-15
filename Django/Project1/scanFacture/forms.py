from django import forms
from django.forms import inlineformset_factory
from .models import Facture, LigneArticle

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['fournisseur', 'numero_facture', 'date_facture', 'montant_ht', 'tva', 'fichier']
        widgets = {
            'fournisseur': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_facture': forms.TextInput(attrs={'class': 'form-control'}),
            'date_facture': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant_ht': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'onchange': 'calculerTTC()'}),
            'tva': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'onchange': 'calculerTTC()'}),
            'fichier': forms.FileInput(attrs={'class': 'form-control', 'accept': '.pdf'})
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.montant_ttc = instance.montant_ht + instance.tva
        if commit:
            instance.save()
        return instance

class LigneArticleForm(forms.ModelForm):
    class Meta:
        model = LigneArticle
        fields = ['designation', 'quantite', 'prix_unitaire']
        widgets = {
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'quantite': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '1', 'onchange': 'calculerTotalArticle(this)'}),
            'prix_unitaire': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0', 'onchange': 'calculerTotalArticle(this)'})
        }

    def clean(self):
        cleaned_data = super().clean()
        quantite = cleaned_data.get('quantite')
        prix_unitaire = cleaned_data.get('prix_unitaire')

        if quantite is not None and prix_unitaire is not None:
            if quantite <= 0:
                raise forms.ValidationError("La quantité doit être supérieure à 0.")
            if prix_unitaire < 0:
                raise forms.ValidationError("Le prix unitaire ne peut pas être négatif.")
        return cleaned_data

LigneArticleFormSet = inlineformset_factory(
    Facture,
    LigneArticle,
    form=LigneArticleForm,
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
    fields=['designation', 'quantite', 'prix_unitaire']
)
