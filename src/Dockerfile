FROM alpine

COPY requirements.txt requirements.txt

RUN apk add --no-cache \
    postgresql-dev \
    libc6-compat \
    alpine-sdk \
    python3-dev \
    py-pip \
    linux-headers \
    python3 && \
    pip3 install --upgrade pip setuptools && \
    pip3 install -r requirements.txt

RUN apk del  \
    alpine-sdk \
    linux-headers

COPY . .