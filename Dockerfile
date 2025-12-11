# Dockerfile — optimized simple image for Streamlit on Fly.io
FROM python:3.11-slim

# System deps (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy code
COPY . /app

# Install Python deps
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Streamlit binding for server
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_ENABLECORS=false
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8080

# Expose the port Streamlit will run on
EXPOSE 8080

# Launch Streamlit on 0.0.0.0:8080
CMD ["streamlit", "run", "green_steel_streamlit_app.py", "--server.port=8080", "--server.address=0.0.0.0", "--server.headless=true"]
