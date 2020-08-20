FROM python:3.6.12-alpine3.12

COPY . /api

WORKDIR /api

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]
