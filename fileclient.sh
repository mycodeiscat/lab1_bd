#!/bin/sh
set -e

docker volume create clientvol

CONTAINER_IP=$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server)

docker run --name client -v clientvol:/clientdata -e IP=$CONTAINER_IP -e PORT=$PORT --network network0 myclient
