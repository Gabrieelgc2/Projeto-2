docker network create flask_redis_net 
docker run -d --name redis --network flask_redis_net redis:alpine 
docker run -d --name flask --network flask_redis_net -p 5000:5000 -e REDIS_HOST=redis flask-app 
docker build -t flask-app . 
curl -X POST -H "Content-Type: application/json" -d '{"key":"curso","value":"docker"}' http://localhost:5000/set 
curl http://localhost:5000/get/curso 
docker logs flask