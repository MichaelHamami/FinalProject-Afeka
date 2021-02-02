FROM python:3.8-alpine

# set environment variables
ENV PATH="/scripts:${PATH}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies and dev dependencies
RUN apk update && apk add gcc postgresql-dev zlib-dev jpeg-dev  python3-dev libressl-dev libffi-dev musl-dev libc-dev openssl-dev linux-headers && pip3 install --upgrade pip
# install dependencies
RUN pip install --upgrade pip
RUN pip install cryptography==2.1.4

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
# RUN pip uninstall PIL
RUN pip install Pillow

# COPY ./user_problems_db.sh /docker-entrypoint-initdb.d/user_problems_db.sh

RUN mkdir /sql_training
COPY ./sql_training /sql_training
WORKDIR /sql_training

EXPOSE 8000

COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web
USER user
CMD ["entrypoint.sh"]