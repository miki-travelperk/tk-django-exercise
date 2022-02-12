from django.test import TestCase

from recipe import models


def sample_recipe(name='Test Recipe', description='Test Recipe Description'):
    return models.Recipe.objects.create(name=name, description=description)


class ModelsTests(TestCase):

    def test_ingredient_str(self):
        """test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            name='Ingredient test name',
            recipe=sample_recipe()
        )
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """test the recipe string representation"""
        recipe = sample_recipe()
        self.assertEqual(str(recipe), recipe.name)

    def test_recipe_has_ingredients(self):
        """test that a recipe can contain multiple ingredients"""
        recipe = sample_recipe()
        ingredient1 = models.Ingredient.objects.create(
            name='Ingredient 1',
            recipe=recipe
        )
        ingredient2 = models.Ingredient.objects.create(
            name='Ingredient 2',
            recipe=recipe
        )
        ingredients = models.Ingredient.objects.all()
        self.assertEqual(len(ingredients), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients)
