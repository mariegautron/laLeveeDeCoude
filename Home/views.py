from django.shortcuts import render
from Recipe.models import Category, Recipe, User
from Ingredient.models import Ingredient
from django.http import Http404
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    latest_recipe = Recipe.objects.order_by('created_at')[:4]
    categories = Category.objects.all()
    users = User.objects.all()
    ingredients = Ingredient.objects.all()
    
    context = { "latest_recipe": latest_recipe, "categories": categories, "ingredients": ingredients, "users": users}
    if request.user:
        return render(request, 'home.html', context)
    else:
        print("User isn't authenticated")
        return render(request, 'home.html')

def latest_recipe_list(request):
    return render(request, "last-recipe.html")
