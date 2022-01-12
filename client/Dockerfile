FROM python:3.11-rc-alpine

RUN pip install requests

RUN mkdir /entrypoint

WORKDIR /entrypoint

COPY ./client.py ./client.py

ENTRYPOINT python3 client.py $IP $PORT

