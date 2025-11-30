docker rm -f redis
docker run -d --name redis --network flask_redis_net -v redis_data:/data redis:alpine