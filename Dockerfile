# Базовий образ
FROM python:3.11-slim

# ставимо Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    curl \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Робоча директорія
WORKDIR /greencity

# Копіюємо requirements окремо (для кешу)
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проєкт
COPY . .

# Команда запуску тестів
CMD ["pytest", "-v"]
