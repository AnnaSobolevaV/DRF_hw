FROM python:3.12-slim

RUN apt-get update && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /courses_app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false &&  \
    poetry install --no-root

COPY . .

EXPOSE 8000
