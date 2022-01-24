# Travelperk Django Exercise

Training exercise during the onboarding to get familiar with django and its ecosystem

Description/requirements of the API on `specs.md`

The solution runs containerized with two containers: one for database (postgresql) and the other one the application itself (running on django test http server). There are som tests to check commands (wait_for_db), models (ingredient and recipe), serializers (ingredient and recipe) and the REST API itself (for recipe endpoint)

## Commands

### Run tests

`make test`

### Run containers to access REST API

`make run`

The API will be available at http://127.0.0.1:8000/recipes [GET, POST, PATCH, DELETE and PUT methods]

## To improve

Easily the exercise could be extended from the initial specs to add user authentication (using a bearer token on headers thru rest_framework TokenAuthentication on authentication_classes). Add user as a owner (foreign key) of the recipe (and ingredients) and separating Public from Private part in the API (i.e: only allow to list existing recipes if you're not authenticated).