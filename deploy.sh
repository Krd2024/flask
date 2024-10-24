#!/bin/bash

# Строим новый Docker-образ
docker build -t flask_web .

# Останавливаем и удаляем предыдущий контейнер, если он запущен
docker stop flask_web_1 || true
docker rm flask_web_1 || true

# Запускаем новый контейнер
docker run -d --name flask_web_1 -p 5000:5000 flask_web 

echo "Flask приложение обновлено и запущено на http://localhost:5000"
