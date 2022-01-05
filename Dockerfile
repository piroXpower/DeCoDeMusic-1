FROM python:3.9.7-slim-buster
RUN apt-get update && apt-get upgrade -y
RUN python3 -m pip install --upgrade pip
RUN pip3 uninstall pyrogram -y
RUN pip3 install git+https://github.com/pyrogram/pyrogram@master
COPY . /app
WORKDIR /app
RUN python3.9 -m pip install -U -r requirements.txt
CMD python3.9 main.py
