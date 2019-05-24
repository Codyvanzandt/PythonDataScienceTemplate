FROM gitpod/workspace-full

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt
