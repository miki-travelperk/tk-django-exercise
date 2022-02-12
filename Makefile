build-container:
	docker build .

test:
	docker-compose run --rm app sh -c "python manage.py test && flake8"

migrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations recipe"

run:
	docker-compose up

curl:
	./curls.sh $(recipeid)