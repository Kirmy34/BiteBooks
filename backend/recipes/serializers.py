from rest_framework import serializers
from django.db import transaction
from .models import Ingredient, Tag, Recipe, RecipeIngredient

# --- Ingredient Serializer ---
# Handles conversion of Ingredient model to/from JSON
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

# --- Tag Serializer ---
# Handles conversion of Tag model to/from JSON
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

# --- RecipeIngredient Serializer ---
# Handles the intermediate model linking Recipes and Ingredients, including quantities and units
class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.ReadOnlyField(source='ingredient.name')

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'ingredient_name', 'quantity', 'unit']

# --- Recipe List Serializer (Lite) ---
# Optimized for high-performance recipe cards/lists by excluding instructions and full ingredient lists
class RecipeListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'name', 'description', 'tags', 'created_at']

# --- Recipe Detail Serializer (Full) ---
# Handles the full recipe details including instructions and nested ingredients. Used for retrieve/create/update.
class RecipeSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Tag.objects.all(), source='tags'
    )
    # This field handles both reading (output) and writing (input) for nested ingredients
    recipe_ingredients = RecipeIngredientSerializer(source='recipeingredient_set', many=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'name', 'description', 'instructions', 
            'tags', 'tag_ids', 'recipe_ingredients', 'created_at'
        ]

    @transaction.atomic
    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        ingredients_data = validated_data.pop('recipeingredient_set', [])
        
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags_data)

        for ingredient_data in ingredients_data:
            RecipeIngredient.objects.create(recipe=recipe, **ingredient_data)
            
        return recipe

    @transaction.atomic
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        ingredients_data = validated_data.pop('recipeingredient_set', None)

        # Update basic recipe fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update tags if provided
        if tags_data is not None:
            instance.tags.set(tags_data)

        # Update ingredients if provided (Replace strategy)
        if ingredients_data is not None:
            instance.recipe_ingredients.all().delete()
            for ingredient_data in ingredients_data:
                RecipeIngredient.objects.create(recipe=instance, **ingredient_data)

        return instance
