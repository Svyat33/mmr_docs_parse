FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt ./
RUN pip install -U pip && pip install --no-cache-dir -r requirements.txt
COPY . .
CMD exec python main.py