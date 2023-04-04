FROM python:3.11.2-slim-bullseye

WORKDIR code
COPY ./smoke .
EXPOSE 8000:8000
CMD ["python3", "solution.py"]