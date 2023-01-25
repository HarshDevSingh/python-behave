FROM python:3.8

WORKDIR /tmp
COPY ../requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /var/
RUN mkdir "end_to_end"
WORKDIR /var/end_to_end