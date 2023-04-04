FROM python-3.10-slim-bullseye

WORKDIR code
COPY smoke%20test .
RUN python3 solutions.py