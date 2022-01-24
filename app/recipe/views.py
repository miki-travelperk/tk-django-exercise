from rest_framework import viewsets


from recipe.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()

    # Specification doesn't require auth or permissions, omitting
    authentication_classes = ()
    permission_classes = ()

    def get_queryset(self):
        """retrieve the recipes for the authenticated user"""
        search_name = self.request.query_params.get('name')
        queryset = self.queryset

        if search_name:
            queryset = queryset.filter(name__icontains=search_name)

        return queryset
