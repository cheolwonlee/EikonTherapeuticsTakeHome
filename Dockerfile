# syntax=docker/dockerfile:1
FROM nickgryg/alpine-pandas

EXPOSE 8080

WORKDIR /usr/src/app

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add build-base

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "controller.py"]
