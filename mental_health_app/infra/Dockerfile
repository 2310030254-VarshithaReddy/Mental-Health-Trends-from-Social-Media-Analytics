# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY ../backend /app/backend
COPY ../dashboard /app/dashboard
COPY ../data /app/data

# Install dependencies
COPY ../backend/requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt
RUN pip install streamlit requests pandas matplotlib seaborn

# Expose backend (FastAPI) port and frontend (Streamlit) port
EXPOSE 8000
EXPOSE 8501

# Default command starts both backend and dashboard
CMD bash -c "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run dashboard/app.py --server.port 8501 --server.address 0.0.0.0"
