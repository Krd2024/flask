# Используем официальный базовый образ Ubuntu
# FROM ubuntu:latest
FROM python: 3.9.20-alpine3.19
# Обновляем пакеты и устанавливаем Python3 и pip
RUN apt-get update && apt-get install -y python3 python3-pip 

# # Устанавливаем Flask через pip
# RUN pip3 install flask waitress

# # Копируем ваше приложение в контейнер
# COPY app.py /opt/app.py

# # Устанавливаем рабочую директорию
# WORKDIR /opt
# Устанавливаем зависимости
WORKDIR /opt

# Копируем файл зависимостей (если есть)
COPY requirements.txt /opt/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . /opt
# Открываем порт 5000 для доступа извне
EXPOSE 5000

# Команда для запуска Flask-приложения
ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:5000", "main:app"]


# Устанавливаем переменную окружения
# ENV FLASK_APP=app.py
