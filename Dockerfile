FROM python:3.6-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /code
COPY . /code

RUN pip install -r /code/requirements.txt
RUN chmod 777 /code/start.sh

CMD ["/code/start.sh"]
