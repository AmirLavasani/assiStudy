#
# Dockerfile
#

FROM ubuntu:xenial
MAINTAINER Amir Lavasani "amirm.lavasani@gmail.com"

RUN apt-get update
RUN apt-get install -y python python-pip libicu-dev
RUN apt-get clean
RUN pip install --upgrade pip
RUN mkdir /opt/assistudy
COPY ./* /opt/assistudy/
RUN pip install -r /opt/assistudy/requirements.txt

EXPOSE 5000 5000

WORKDIR /opt/assistudy

CMD python server.py