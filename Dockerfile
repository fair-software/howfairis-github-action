FROM python:3.9-alpine

RUN apk update && apk add build-base

WORKDIR /data
RUN pip install howfairis
ENTRYPOINT ["howfairis"]
