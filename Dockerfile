# Используем образ Python 3.11
FROM python:3.11-slim-buster

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Копируем requirements.txt в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости приложения
RUN pip install --no-cache-dir -r requirements.txt

# Копируем содержимое текущей директории в рабочую директорию контейнера
COPY . .

# Задаем переменную окружения для базы данных SQLite
ENV DATABASE_URL=sqlite:///db.sqlite3

# Запускаем миграции базы данных
RUN python manage.py migrate

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]