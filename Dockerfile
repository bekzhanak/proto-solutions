FROM python:3.11.2-slim-bullseye

WORKDIR code
COPY ./smoke .
RUN python3 smoke/solutions.py