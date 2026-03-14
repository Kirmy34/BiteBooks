from django.db import models

# --- Ingredient Model ---
# Represents a single ingredient in the pantry (e.g., "Salt", "Olive Oil").
# These are shared across multiple recipes.
class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# --- Tag Model ---
# Used for categorizing recipes (e.g., "Breakfast", "Vegan", "Quick & Easy").
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# --- Recipe Model ---
# The core entity representing a full recipe, including metadata and links 
# to tags and ingredients via a through-table.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    instructions = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='recipes', blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        related_name='recipes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# --- RecipeIngredient Model (Through Table) ---
# Links a specific Ingredient to a Recipe and stores recipe-specific data 
# like the required quantity and unit of measurement.
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.CharField(max_length=50) # e.g., grams, cups, tbsp

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} for {self.recipe.name}"
