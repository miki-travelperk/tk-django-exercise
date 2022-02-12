from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from recipe.models import Recipe

RECIPE_BASE_URL = '/recipes/'


def detail_url(recipe_id):
    return f'/recipes/{recipe_id}/'


def sample_payload():
    """creates a sample valid JSON payload for a recipe"""
    return {
        'name': 'test recipe',
        'description': 'description text',
        'ingredients': [
                {'name': 'ingredient 1'},
                {'name': 'ingredient 2'}
        ],
    }


def sample_recipe(ingredients=None):
    """creates a sample recipe with two default ingredients or from params"""
    recipe = Recipe.objects.create(
        name='test recipe',
        description='description text'
    )

    if ingredients:
        for ingredient in ingredients:
            recipe.ingredients.create(name=ingredient)
    else:
        recipe.ingredients.create(name='ingredient 1')
        recipe.ingredients.create(name='ingredient 2')

    return recipe


class PublicRecipeApiTests(TestCase):
    """test unauthenticated Recipe API endpoints"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_recipes(self):
        """test retrieving a list of 3 created recipes"""
        sample_recipe()
        sample_recipe(('dough', 'cheese', 'tomato', 'casa-tarradellas'))
        sample_recipe(('one', 'two', 'three'))

        res = self.client.get(RECIPE_BASE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 3)

    def test_retrieve_single_recipe(self):
        """test retrieving a single recipe (detail view) by id"""
        recipe = sample_recipe()

        res = self.client.get(detail_url(recipe.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['name'], recipe.name)

    def test_create_recipe(self):
        """test adding a new recipe from API"""
        payload = sample_payload()

        res = self.client.post(RECIPE_BASE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        recipe = Recipe.objects.get(id=res.data['id'])
        self.assertEqual(res.data['name'], recipe.name)
        self.assertEqual(
            len(res.data['ingredients']), recipe.ingredients.count())

    def test_replace_ingredients_recipe(self):
        """test replacing all ingredients in existing recipe"""
        recipe_original = sample_recipe()

        self.assertEqual(recipe_original.ingredients.count(), 2)

        payload = {
            'ingredients': [
                {'name': 'one'},
                {'name': 'two'},
                {'name': 'three'},
                {'name': 'four'},
                {'name': 'five'}
            ],
        }

        res = self.client.patch(detail_url(recipe_original.id), payload)

        recipe_original.refresh_from_db()
        recipe = Recipe.objects.get(id=recipe_original.id)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(recipe.ingredients.count(), 5)
        self.assertEqual(recipe.name, recipe_original.name)

    def test_modify_recipe(self):
        """test modifying parameters of a recipe"""
        recipe = sample_recipe()
        payload = sample_payload()

        res = self.client.put(detail_url(recipe.id), payload)
        recipe.refresh_from_db()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(recipe.name, payload['name'])
        self.assertEqual(recipe.ingredients.count(), 2)

    def test_remove_recipe_return_no_content(self):
        """test deleting an existing recipe, return 204 No content"""
        sample_recipe()
        recipe = sample_recipe()
        res = self.client.delete(detail_url(recipe.id))

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Recipe.objects.count(), 1)

    def test_filtering_recipes(self):
        """test filtering by name substring (case insensitive)"""
        sample_recipe()
        sample_recipe(('dough', 'cheese', 'tomato'))
        Recipe.objects.create(
            name='not matching name',
            description='descriptiont text'
        )

        res = self.client.get(RECIPE_BASE_URL + '?name=reci')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)
