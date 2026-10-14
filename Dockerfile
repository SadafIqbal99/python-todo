FROM python:3.11-slim
WORKDIR /app
COPY todo.py .
CMD ["python", "todo.py"]
