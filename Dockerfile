FROM python:alpine
WORKDIR /tests/

COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV ENV=dev

CMD python -m pytest -s -v /tests/
