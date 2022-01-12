FROM python:3.11-rc-alpine

RUN mkdir /entrypoint

WORKDIR /entrypoint

COPY ./server.py ./server.py

ENTRYPOINT python3 server.py $PORT