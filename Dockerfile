FROM python:3.12

WORKDIR /code
WORKDIR /code/requirements.txt

COPY ./requirements.txt /code/requirements.txt

COPY /* /code/
CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","80"]

LABEL authors="joaopedromesquita"
