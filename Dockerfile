FROM python:3.10.3-slim

RUN mkdir my_code
WORKDIR /my_code

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python","main.py"]

