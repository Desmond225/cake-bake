from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Recipe, Rating
from django.http import Http404
from django.shortcuts import get_object_or_404, render
# Create your views here.

def ijsjes(request):
    return render(request, 'cake/ijsjes.html', {'ijsjes': ijsjes})

def koekjes(request):
    return render(request, 'cake/koekjes.html', {'koekjes': koekjes})

def taarten(request):
    return render(request, 'cake/taarten.html', {'taarten': taarten})

def home(request):
    recipe = Recipe.objects
    return render(request, 'cake/base.html', {'recipe':recipe})

def index(request):
    latest_recipe_list = Recipe.objects.order_by('-pub_date')[:5]
    context = {'latest_recipe_list': latest_recipe_list}
    return render(request, 'cake/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'cake/detail.html', {'recipe': recipe})

def ingredients(request, recipe_id):
    return HttpResponse("You're looking at ingredients required for recipe %s." % recipe_id)

def rate(request, recipe_id):
    return HttpResponse("You're rating recipe %s." % recipe_id)

def vote(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    try:
        selected_rating = recipe.rating_set.get(pk=request.POST['recipe'])
    except (KeyError, Rating.DoesNotExist):
        return render(request, 'cake/detail.html', {
        'recipe': recipe,
        'error_message': "Rating not selected - error! .",
        })
    else:
        selected_rating.votes += 1
        selected_rating.save()
        return HttpResponseRedirect(reverse('cake:results', args=(recipe.id,)))

def results(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'cake/results.html', {'recipe':recipe})
