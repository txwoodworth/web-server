FROM python:3.11-slim

WORKDIR /app
COPY webpage.py .  
#index.html

RUN pip install flask requests
EXPOSE 8080
CMD ["python", "webpage.py"]
