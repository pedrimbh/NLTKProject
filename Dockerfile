FROM python

WORKDIR /code
WORKDIR /code/requirements.txt

COPY ./requirements.txt /code/requirements.txt

RUN pip install  -r requirements.txt

COPY ./  /code/
CMD ["uvicorn", "main:app","--host","0.0.0.0","--port","80"]

LABEL authors="joaopedromesquita"
