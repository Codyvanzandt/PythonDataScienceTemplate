FROM gitpod/workspace-full

USER root

RUN sudo python3 -m pip install -r ./requirements.txt

USER gitpod
