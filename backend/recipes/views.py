from rest_framework import viewsets
from .models import Ingredient, Tag, Recipe
from .serializers import (
    IngredientSerializer, 
    TagSerializer, 
    RecipeSerializer, 
    RecipeListSerializer
)

# --- Ingredient ViewSet ---
# Provides full CRUD (Create, Read, Update, Delete) for the Ingredient pantry
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

# --- Tag ViewSet ---
# Provides full CRUD for recipe categorization tags
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# --- Recipe ViewSet ---
# Provides optimized CRUD for Recipes. 
# Automatically switches between "Lite" (list) and "Full" (detail) serializers for efficiency.
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.prefetch_related(
        'tags',
        'recipeingredient_set__ingredient'
    ).all()

    def get_serializer_class(self):
        # Use the "Lite" serializer for the list view (Cards)
        if self.action == 'list':
            return RecipeListSerializer
        # Use the "Full" serializer for detail view, create, and update
        return RecipeSerializer
