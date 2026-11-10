FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY calculator.py .
EXPOSE 8000
CMD ["python", "calculator.py"]
