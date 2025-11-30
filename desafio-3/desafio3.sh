docker rm -f flask redis
docker network rm flask_redis_net
docker compose up --build