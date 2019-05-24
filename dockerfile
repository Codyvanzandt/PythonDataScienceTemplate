FROM gitpod/workspace-full

USER root

RUN sudo pip3 install -r ./requirements.txt

USER gitpod
