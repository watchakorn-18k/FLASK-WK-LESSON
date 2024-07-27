FROM python:3.11.5-alpine
WORKDIR /web_app
COPY . .
RUN apk add postgresql-dev gcc musl-dev
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
EXPOSE 5000
ENTRYPOINT ["flask","run","--host=0.0.0.0"]