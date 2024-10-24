#!/bin/bash

# Остановить текущий контейнер
docker stop flask_web_1 || true

# Удалить текущий контейнер
docker rm flask_web_1 || true

# Пересобрать образ
docker-compose up -d --build

echo "Flask приложение обновлено и на http://localhost:5000"
