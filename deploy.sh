#!/bin/bash

# Остановить текущий контейнер
docker stop flask_web_1 || true

# Удалить текущий контейнер
docker rm flask_web_1 || true

docker-compose down

# Удаляем неиспользуемые образы
# docker image prune -f

# # Запускаем проект
# docker-compose up -d --build
docker-compose up -d --build && docker image prune -f

# Удаляем неиспользуемые образы
docker image prune -f
echo "Flask приложение обновлено и на http://localhost:5000"
