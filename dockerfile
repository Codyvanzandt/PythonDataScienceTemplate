FROM gitpod/workspace-full

USER root

RUN pip install -r ./requirements.txt

USER gitpod
