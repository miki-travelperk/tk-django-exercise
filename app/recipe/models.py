from django.db import models


class Recipe(models.Model):
    """recipe object"""
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """ingredient to be used in a recipe"""
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        to=Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
