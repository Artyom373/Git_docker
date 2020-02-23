FROM python:3.6

RUN mkdir -p /usr/scr/app/
WORKDIR /usr/scr/app/

COPY . /usr/scr/app/
RUN pip inastall --no-cash-dir -r requirements.txt

CMD ["python", "Hello.py"]
