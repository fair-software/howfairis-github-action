FROM python:3.12-alpine

RUN apk update && apk add --no-cache build-base

WORKDIR /data

RUN python3 -m pip install --upgrade pip wheel && \
    python3 -m pip install howfairis

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
