FROM ubuntu:18.04

LABEL maintainer="AlphaRead"

RUN apt-get update && apt-get install -y python3 \
    python3-pip

RUN apt-get install -y ffmpeg

#RUN apt install build-essential -y
RUN pip3 install setuptools pip --upgrade --force-reinstall

COPY ./requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /app
COPY ./app /app
COPY ./run.py /run.py
COPY ./wsgi.ini /wsgi.ini

EXPOSE 80
EXPOSE 5000

CMD ["uwsgi", "--ini", "/app/wsgi.ini"]
# CMD ["/bin/ash"]