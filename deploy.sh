#!/bin/bash

# Строим новый Docker-образ
docker build -t my-flask-app .

# Останавливаем и удаляем предыдущий контейнер, если он запущен
docker stop flask-app || true
docker rm flask-app || true

# Запускаем новый контейнер
docker run -d --name flask-app -p 5000:5000 my-flask-app

echo "Flask приложение обновлено и запущено на http://localhost:5000"
