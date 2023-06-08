FROM python:3.10

ADD main.py .
ADD config.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]
