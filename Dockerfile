FROM python:3.10

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
COPY . .

RUN apt-get update && apt-get install -y wget unzip && \
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
   apt install -y ./google-chrome-stable_current_amd64.deb && \
   remote google-chrome-stable_current_amd64.deb && \
   apt-get clean


CMD [ "python","main.py"]