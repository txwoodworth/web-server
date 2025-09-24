FROM python:3.11-slim
WORKDIR /app
COPY webcam.py .
COPY test_image.jpg .
RUN pip install flask
EXPOSE 8082
CMD ["python","webcam.py"]
