FROM --platform=linux/amd64 python:3.10

WORKDIR /python-docker

# Copy only requirements.txt first to leverage caching
COPY requirements.txt /python-docker/
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

RUN apt-get update && apt-get install -y wget unzip ffmpeg

RUN apt-get install -y chromium chromium-driver


# # Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DISPLAY=:99 \
    CHROME_BIN=/usr/bin/chromium

# Copy application code last (this layer changes frequently)
COPY . /python-docker    

CMD [ "python","test.py"]

