from rest_framework import serializers

from recipe.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """serializer for ingredient objects"""

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeSerializer(serializers.ModelSerializer):
    """serialize recipe object"""

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ("id", "name", "description", "ingredients")
        read_only_fields = ("id",)

    def create(self, validated_data):
        ingredients = validated_data.pop("ingredients")
        recipe = super().create(validated_data)

        for ingredient in ingredients:
            recipe.ingredients.create(**ingredient)

        return recipe

    def update(self, instance, validated_data):
        ingredients = validated_data.pop("ingredients", None)
        recipe = super().update(instance, validated_data)

        if ingredients:
            recipe.ingredients.all().delete()
            for ingredient in ingredients:
                recipe.ingredients.create(**ingredient)

        return recipe
