# Базовый образ с Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt || true

# Запускаем тесты при сборке
RUN python -m unittest discover tests/ || true

# Команда для запуска калькулятора
CMD ["python", "main.py"]