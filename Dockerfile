FROM python:3.11.2-slim-bullseye

WORKDIR code
COPY smoke%20test .
RUN python3 solutions.py