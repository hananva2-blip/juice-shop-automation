FROM jenkins/jenkins:lts-jdk21

USER root
# Python + the system libraries Chromium needs
RUN apt-get update && apt-get install -y python3 python3-venv python3-pip \
    && pip3 install --break-system-packages playwright \
    && playwright install-deps chromium \
    && rm -rf /var/lib/apt/lists/*
USER jenkins

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt
COPY casc.yaml /casc.yaml
