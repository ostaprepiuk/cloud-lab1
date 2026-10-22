# Використовуємо зафіксовану slim-версію
FROM python:3.11-slim-bookworm

# Створюємо непривілейованого користувача
RUN useradd -m -r appuser
WORKDIR /app

# Копіюємо лише requirements для кешування шару залежностей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код застосунку
COPY . .

# Передаємо права користувачу
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]