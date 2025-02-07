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



# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY app app
COPY migrations migrations
COPY appserver.py config.py ./
COPY ./scripts/boot.sh ./
RUN chmod a+x ./boot.sh



# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
#USER appuser


ENV FLASK_ENV=development
ENV PORT=8000
ENV HOST=0.0.0.0

EXPOSE 8000
ENTRYPOINT [ "./boot.sh" ] 