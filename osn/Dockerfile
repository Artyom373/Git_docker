FROM python:3.6

RUN mkdir -p /usr/scr/app/
WORKDIR /usr/scr/app/

COPY . /usr/scr/app/
RUN pip install --no-cash-dir -r -y requirements.txt

CMD ["python", "Hello.py"]
