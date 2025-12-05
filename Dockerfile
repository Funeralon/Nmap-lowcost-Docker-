FROM python:3.9-slim

WORKDIR /app

COPY scanner.py .

RUN useradd -m monuser
USER monuser

CMD ["python", "-u", "scanner.py"]