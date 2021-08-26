FROM python:3.8.11-slim

WORKDIR /opt/program

COPY python/ .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
