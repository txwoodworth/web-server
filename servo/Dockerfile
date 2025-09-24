FROM python:3.11-slim

WORKDIR /app
COPY servo.py .

RUN pip install flask smbus2
EXPOSE 8081
CMD ["python", "servo.py"]
