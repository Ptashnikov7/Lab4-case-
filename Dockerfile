# Модель: Метод Ньютона (5 семестр)
# Автор: Пташников Василь, група АІ-235

FROM python:3.11-slim
WORKDIR /app
COPY main.py .

# Налаштування змінних середовища за замовчуванням
ENV STUDENT_NAME="Пташников Василь"
ENV GROUP="АІ-235"
ENV MODE="eco" 
ENV SERVICE_PORT=8000

EXPOSE 8000
CMD ["python", "main.py"]
