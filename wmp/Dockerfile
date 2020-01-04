# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7.5-alpine

RUN apk add --update --no-cache \
    g++ gcc libxslt-dev musl-dev python3-dev \
    libffi-dev openssl-dev jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

WORKDIR /usr/src/wmp
COPY ./requirements.txt /usr/src/wmp

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#ENTRYPOINT ["python"]
COPY . /usr/src/wmp
