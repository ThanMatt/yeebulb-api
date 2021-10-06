FROM python:3.8-alpine

WORKDIR /usr/yeebulb-api

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000