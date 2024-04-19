FROM python:3.12-bullseye

RUN apt-get update && \
    apt-get install -y poppler-utils

WORKDIR /work

COPY requirements.txt /work

ENV VIRTUAL_ENV=/usr/local
RUN pip install uv && uv pip install --no-cache -r requirements.txt

COPY /work /work

CMD ["/bin/sh"]