FROM python:3.9.6

RUN mkdir -p /pip_resolver/lib
COPY lib /pip_resolver/lib

RUN mkdir -p /pip_resolver/app
COPY app/x/ /pip_resolver/app/x/

WORKDIR /pip_resolver/app/x
RUN pip install -r requirements.txt

CMD ["python", "app.py"]

