docker network create network0

docker volume create servervol

docker run --name server -v servervol:/serverdata -e PORT=$PORT --network network0 myserver
