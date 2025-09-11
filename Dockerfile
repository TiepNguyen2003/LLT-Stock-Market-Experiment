# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.12

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*\
  pkg-config
# Allows pings
RUN apt-get update 
RUN apt-get install iputils-ping -y

WORKDIR /helia_app
  
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy app files into the working directory
COPY ./app ./app
COPY appserver.py config.py wsgi.py ./
RUN mkdir data

# Run Startup
COPY ./startup.sh ./startup.sh
RUN chmod +x ./startup.sh
RUN ./startup.sh

# Copy and set permission for boot script
COPY ./boot.sh ./boot.sh
RUN chmod +x ./boot.sh




# Run the app
CMD ["bash", "./boot.sh"]