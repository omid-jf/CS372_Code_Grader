FROM python:3.10-slim-bullseye

WORKDIR /app
COPY requirements.txt /root/

RUN apt-get update && apt-get install -y  \
    g++  \
    wget

RUN wget https://download.oracle.com/java/18/latest/jdk-18_linux-x64_bin.deb && \
    apt-get install -y ./jdk-18_linux-x64_bin.deb && \
    rm ./jdk-18_linux-x64_bin.deb

ENV JAVA_HOME=/usr/lib/jvm/jdk-18/
ENV PATH=$PATH:$JAVA_HOME/bin

RUN pip install --no-cache-dir -r /root/requirements.txt

ENTRYPOINT ["python", "main.py"]
