test:
	poetry run pytest

format:
	poetry run black .
	isort .

lightsail-push:
	aws lightsail push-container-image --service-name mazegen2 --label mazegen2 --image mazegen2

docker-build:
	docker build -t mazegen2 .

docker-run:
	docker run -p 5069:5000 mazegen2 poetry run flask run --host 0.0.0.0