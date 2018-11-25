FROM ubuntu

MAINTAINER Leon Nascimento <leonfnasc@gmail.com>

RUN apt-get update
RUN apt-get install -y postgresql
RUN apt-get install python3
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install psycopg2
RUN pip install postgres
RUN apt-get install -y vim

EXPOSE 5000

RUN mkdir /project/
RUN mkdir /project/model
COPY ./* /project/
RUN mv /project/*py /project/model
RUN rm /project/*pyc
RUN mv project/model/app.py /project
WORKDIR /project/

