FROM python:3.9-alpine

WORKDIR /data
RUN pip install howfairis
ENTRYPOINT ["howfairis"]
