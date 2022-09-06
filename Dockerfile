FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY run.py .
COPY app .
COPY data .
COPY logs .
COPY static .
COPY templates .
COPY tests .

CMD flask run -h 0.0.0.0 -p 80
