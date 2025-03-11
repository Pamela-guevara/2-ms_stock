# 2-ms_stock

This repository is a microservice of "e-commerce" proyect, made with saga pattern.

# 1-ms_products

This repository is a microservice of "e-commerce" proyect, made with saga pattern.

To initialize, first download the repositories belonging to this project, which are:

- e-commerce
- ms_payments
- ms_purchases
- ms_products
- ms_stocks
- postgres
- docker

Then, create an image of each repository containing the microservices, except for the "postgres" and "docker" microservice, using the `docker build` command within each microservice.

Create a container in docker for the Redis service, with port 6379, and get it running.

From the "postgres" microservice, bring up this container with `docker compose up`.

From the "docker" microservice, bring up the entire project with the `docker compose up` command.

### At this point, the e-commerce project should be running; if it is not, review each step again.

---

# En español:

Para inicializarlo, descargue primero los repositorios pertenecientes a este proyecto, que son:

- e-commerce
- ms_payments
- ms_purchases
- ms_products
- ms_stocks
- postgres
- docker
  Luego, cree una imagen de cada repositorio que contiene a los microservicios, a excepción del
  microservicio "postgres" y "docker", con el comando "docker build" dentro de cada microservicio.
  Cree un contenedor en docker del servicio Redis, con el puerto 6379 y póngalo en funcionamiento.
  Desde el microservicio "postgres", levante este contenedor con "docker compose up".
  Desde el microservicio "docker", levante el proyecto completo con el comando "docker compose up".
  En este punto, el proyecto de e-commerce debería estar en funcionamiento; en caso de no estarlo,
  revise cada paso nuevamente.
