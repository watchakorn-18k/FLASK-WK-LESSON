FROM python:3.10.14-alpine3.20
WORKDIR /web_app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=run.py
ENTRYPOINT ["flask","run","--host=0.0.0.0"]