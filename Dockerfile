FROM python:3.10-slim

WORKDIR /usr/src/app

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app
COPY ./nginx.conf /etc/nginx/nginx.conf

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:4500", "app:app"]
