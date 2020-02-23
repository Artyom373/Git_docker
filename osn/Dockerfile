FROM python:3.6

RUN mkdir -p /usr/scr/app/
WORKDIR /usr/scr/app/

COPY . /usr/scr/app/
RUN pip install -y flask

CMD ["python", "Hello.py"]
