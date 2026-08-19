
FROM python:3.10-slim


WORKDIR /app


COPY . .


RUN pip install --no-cache-dir -r requirements.txt || true


RUN python -m unittest discover tests/ || true


CMD ["python", "main.py"]