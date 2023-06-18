FROM python:3.9.17

RUN apt-get update

RUN apt-get -y install nano
RUN apt-get -y install netbase
RUN apt-get -y install supervisor

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["supervisord","-c","/app/supervisor/services.conf"]