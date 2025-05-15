from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import FactureForm, LigneArticleFormSet
from .models import Facture
from django.core.paginator import Paginator
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

@login_required
def ajouter_facture(request):
    if request.method == 'POST':
        facture_form = FactureForm(request.POST, request.FILES)
        formset = LigneArticleFormSet(request.POST)
        
        if facture_form.is_valid() and formset.is_valid():
            facture = facture_form.save(commit=False)
            facture.utilisateur = request.user
            facture.save()
            
            formset.instance = facture
            formset.save()
            
            logger.info(f"Facture ajoutée avec succès: {facture.id} - {facture.fournisseur}")
            messages.success(request, 'Facture ajoutée avec succès!')
            return redirect('liste_factures')
        else:
            logger.error(f"Erreurs de validation: {facture_form.errors} - {formset.errors}")
            messages.error(request, 'Erreur lors de l\'ajout de la facture. Veuillez vérifier les informations.')
    else:
        facture_form = FactureForm()
        formset = LigneArticleFormSet()
    
    return render(request, 'scanFacture/ajouter-facture.html', {
        'facture_form': facture_form,
        'formset': formset
    })

@login_required
def modifier_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id, utilisateur=request.user)
    
    if request.method == 'POST':
        facture_form = FactureForm(request.POST, request.FILES, instance=facture)
        formset = LigneArticleFormSet(request.POST, instance=facture)
        
        if facture_form.is_valid():
            try:
                with transaction.atomic():
                    facture = facture_form.save(commit=False)
                    facture.utilisateur = request.user
                    facture.save()
                    
                    if formset.is_valid():
                        formset.save()
                        logger.info(f"Facture modifiée avec succès: {facture.id} - {facture.fournisseur}")
                        messages.success(request, 'Facture modifiée avec succès!')
                        return redirect('liste_factures')
                    else:
                        logger.error(f"Erreurs de validation du formset: {formset.errors}")
                        messages.error(request, 'Erreur lors de la modification des articles.')
            except Exception as e:
                logger.error(f"Erreur lors de la modification de la facture: {str(e)}")
                messages.error(request, f'Erreur lors de la modification: {str(e)}')
        else:
            logger.error(f"Erreurs de validation du formulaire facture: {facture_form.errors}")
            messages.error(request, 'Erreur lors de la modification. Veuillez vérifier les informations.')
    else:
        facture_form = FactureForm(instance=facture)
        formset = LigneArticleFormSet(instance=facture)
    
    return render(request, 'scanFacture/modifier-facture.html', {
        'facture_form': facture_form,
        'formset': formset,
        'facture': facture
    })

@login_required
def liste_factures(request):
    factures = Facture.objects.filter(utilisateur=request.user).order_by('-date_facture')
    logger.info(f"Nombre de factures trouvées pour l'utilisateur {request.user.id}: {factures.count()}")
    
    paginator = Paginator(factures, 10)  
    page = request.GET.get('page')
    factures_page = paginator.get_page(page)
    
    return render(request, 'scanFacture/liste-factures.html', {
        'factures': factures_page
    })

@login_required
def detail_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id, utilisateur=request.user)
    return render(request, 'scanFacture/detail-facture.html', {
        'facture': facture
    })

@login_required
def supprimer_facture(request, facture_id):
    if request.method == 'POST':
        facture = get_object_or_404(Facture, id=facture_id, utilisateur=request.user)
        facture.delete()
        messages.success(request, 'Facture supprimée avec succès!')
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
