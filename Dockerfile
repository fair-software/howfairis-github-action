FROM python:3.9-alpine

RUN apk update && apk add --no-cache build-base

WORKDIR /data

RUN python3 -m venv venv            && \
    source venv/bin/activate        && \
    pip install --upgrade pip wheel && \
    pip install howfairis

ENV PATH=/data/venv/bin:${PATH}

ENTRYPOINT ["howfairis"]
