from django.test import TestCase
from recipe.models import Ingredient, Recipe
from recipe.serializers import IngredientSerializer, RecipeSerializer
from recipe.tests.test_recipe_api import sample_payload, sample_recipe


class SerializersTests(TestCase):

    def test_serializer_recipe(self):
        """test serializer for recipe object"""
        recipe = sample_recipe()

        serializer = RecipeSerializer(recipe)
        data = serializer.data

        self.assertEqual(data['id'], recipe.id)
        self.assertEqual(data['name'], recipe.name)
        self.assertEqual(len(data['ingredients']), recipe.ingredients.count())

    def test_serializer_ingredient(self):
        """test serializer for ingredient object"""
        recipe = sample_recipe()
        test_name = 'test_ingredient'
        ingredient = Ingredient.objects.create(
            recipe=recipe,
            name=test_name
        )
        serializer = IngredientSerializer(ingredient)
        self.assertEqual(serializer.data['name'], test_name)

    def test_new_recipe(self):
        """test serializer with new recipe with 3 ingredients"""
        data = sample_payload()
        data['ingredients'].append({'name': 'ingredient 3'})

        serializer = RecipeSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(Recipe.objects.count(), 1)
        self.assertEqual(Ingredient.objects.count(), 3)

    def test_change_recipe(self):
        """test serializer after changing recipe name"""
        recipe = sample_recipe()
        data = sample_payload()
        data['name'] = 'changed name'

        serializer = RecipeSerializer(recipe, data=data)
        self.assertTrue(serializer.is_valid())

        serializer.save()

        self.assertEqual(serializer.data['name'], data['name'])
