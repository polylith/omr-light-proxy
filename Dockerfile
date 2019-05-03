FROM python:3.6

WORKDIR /app
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . .

CMD python server.py