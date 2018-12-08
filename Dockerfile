#
# Dockerfile
#

FROM ubuntu:xenial
MAINTAINER Amir Lavasani "amirm.lavasani@gmail.com"

RUN apt-get update
RUN apt-get install -y python
RUN /usr/bin/python get-pip.py 
RUN apt-get clean
RUN mkdir /opt/assistudy

ADD ./* /opt/assistudy

EXPOSE 5000 5000

WORKDIR /opt/assistudy

CMD python server.py