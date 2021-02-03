FROM python:3.6.12-alpine3.12

MAINTAINER Evan Fairchild "evfairchild@gmail.com"

COPY /api /api/
COPY /twitter /api/twitter
COPY requirements.txt /api
COPY /twitter/secrets.py /api
COPY /twitter/stopwords.txt /api

WORKDIR /api

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main.py"]
