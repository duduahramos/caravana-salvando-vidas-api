# docker run --name mysql-flask-db --publish 1234:3306 mysql:latest

# Base image
FROM python:3.9.13

# MAINTAINER of the Dockerfile
MAINTAINER Eduardo <eduardoahramos@outlook.com>

# WORKING DIRECTORY INSIDE APP
WORKDIR /app

COPY . /app

RUN ls -la

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["flask", "--app", "app/app", "run"]