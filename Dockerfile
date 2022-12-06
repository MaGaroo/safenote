FROM python:3

RUN apt-get update && apt-get install -y procps netcat net-tools wget
COPY requirements.txt /root/

RUN pip install -r /root/requirements.txt

COPY src/ /root/src/
WORKDIR /root/src

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]
