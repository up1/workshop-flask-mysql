FROM python:3.9.0-alpine3.12
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip install --upgrade pip setuptools
RUN pip install pendulum service_identity
WORKDIR /app
RUN pip install PyMySQL
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]