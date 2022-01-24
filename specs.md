# Travelperk Django Exercise

Create a CRUD API with Django and DRF that allows you to CRUD recipes and add/delete ingredients to it.
Test it using postman or similar.
Create automated tests for every action.

## Models

Recipe:

- Name
- Description

Ingredient: 

- Name
- Recipe (ForeignKey, assume a given ingredient belongs only to one recipe, even if that means multiple Ingredient instances with the exact same name).

## Examples

### GET /recipes/1/

```
{
    “id”: 1,
    “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}
```

### POST /recipes/

Creation request

```
{
    “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}

```

Creation response

```
{
    “id”: 1,
    “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
}

```

### GET /recipes/

List recipes

```
[
    {
    “id”: 1,
      “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
    }
]
```

### GET /recipes/?name=Pi

Add search view by name substring

```
[
    {
      “id”: 1,
    “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [{“name”: “dough”}, {“name”: “cheese”}, {“name”: “tomato”}]
    }
]
```

### PATCH /recipes/1/

Request

```
{
“name”: “Pizza”
“description”: “Put it in the oven”,
“ingredients”: [{“name”: “casa-tarradellas”}]
}
```

Should delete the previous existing ingredients and put “casa-tarradellas” as only ingredient for recipe.

Response:
```
{
    “id”: 1,
    “name”: “Pizza”
    “description”: “Put it in the oven”,
    “ingredients”: [{“name”: “casa-tarradellas”}]
}
```

### DELETE /recipes/1/

Should delete the targeted recipe AND its ingredients.

Response:
HTTP 204 (NO CONTENT)

