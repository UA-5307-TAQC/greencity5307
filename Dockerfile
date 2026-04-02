# Використовуємо полегшений офіційний образ Python 3.12
FROM python:3.12-slim

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Оновлюємо пакети та встановлюємо Chromium + ChromeDriver
# --no-install-recommends зменшує розмір образу (оптимізація ⭐)
RUN apt-get update && apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Налаштовуємо системні змінні, щоб Selenium знав, де лежить браузер
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_BIN=/usr/bin/chromedriver

# Копіюємо ТІЛЬКИ requirements.txt для правильного кешування шарів
COPY requirements.txt .

# Встановлюємо залежності без збереження кешу pip
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь інший код проєкту
COPY . .

# Команда за замовчуванням
CMD ["behave"]