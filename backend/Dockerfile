FROM python:3.9.0-alpine3.12
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip install --upgrade pip setuptools
RUN pip install pendulum service_identity
WORKDIR /src
RUN pip install PyMySQL
COPY requirements.txt /src/requirements.txt
RUN pip install -r requirements.txt
COPY . /src

# Testing and coverage
RUN PYTHONPATH=. pytest -v
RUN coverage run -m pytest && coverage report && coverage html

ENTRYPOINT ["python"]
CMD ["app.py"]