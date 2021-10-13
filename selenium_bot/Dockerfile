FROM python:3

COPY requirements.txt ./
COPY ./src/* ./

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]