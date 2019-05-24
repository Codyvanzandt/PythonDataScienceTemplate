FROM gitpod/workspace-full

USER root

RUN pip3 install -r requirements.txt

USER gitpod
