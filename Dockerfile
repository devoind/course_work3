FROM python:3.10

WORKDIR /code

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
COPY run.py .
COPY app app
COPY data data
COPY logs logs
COPY static static
COPY templates templates
USER api
ENV FLASK_APP=run.py

CMD flask run -h 0.0.0.0 -p 80
