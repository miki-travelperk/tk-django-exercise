#!/bin/bash

RECIPE_ID=${1:-1}

# GET (list all recipes)
echo -e "\n"
curl http://127.0.0.1:8000/recipes/
echo -e "\n"

# POST (create recipe)
echo -e "\n"
curl -X POST http://127.0.0.1:8000/recipes/ -H 'Content-Type: application/json' -d '{ "name": "test name","description": "test descr","ingredients": [{"name": "ingredient 2"},{"name": "ingredient 1"}]}'
echo -e "\n"

# GET (detail of specific recipe)
echo -e "\n"
curl http://127.0.0.1:8000/recipes/$RECIPE_ID/
echo -e "\n"

# PATCH (replace ingredients)
echo -e "\n"
curl -X PATCH http://127.0.0.1:8000/recipes/$RECIPE_ID/ -H 'Content-Type: application/json' -d '{ "name": "test name","description": "test descr","ingredients": [{"name": "casa-tarradellas"}]}'
echo -e "\n"

# PUT (replace recipe values)
echo -e "\n"
curl -X PUT http://127.0.0.1:8000/recipes/$RECIPE_ID/ -H 'Content-Type: application/json' -d '{ "name": "test name replaces","description": "new description","ingredients": []}'
echo -e "\n"

# DELETE (removes recipe from DB)
echo -e "\n"
curl -v -X DELETE http://127.0.0.1:8000/recipes/$RECIPE_ID/
echo -e "\n"