FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
HEALTHCHECK --interval=5s --timeout=2s --start-period=5s --retries=3 CMD curl -f http://localhost:5000/health || exit 1
EXPOSE 5000
CMD ["python", "app.py"]
