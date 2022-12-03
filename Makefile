start: build-frontend run-backend

run-backend:
	flask --app backend run

run-frontend:
	npx parcel front/index.html

build-frontend:
	npx parcel build front/index.html --dist-dir front-build

.PHONY: run-backend