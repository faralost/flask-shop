FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libffi-dev
RUN apt-get install -y netcat

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]