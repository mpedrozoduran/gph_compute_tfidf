FROM python:3.8-buster

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY blueprints ./blueprints
COPY scraping ./scraping
COPY compute ./compute
COPY utils ./utils
COPY static ./static
COPY config ./config

EXPOSE 5000

ENV FLASK_APP=main.py
ENV ENV=dev

CMD ["flask", "run", "--host=0.0.0.0"]