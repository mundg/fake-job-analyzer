FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN python -c "import nltk; nltk.download('punkt')"

# Copy the rest of the application files
COPY app.py ./
COPY scripts/predict.py ./scripts/
COPY scripts/preprocessing.py ./scripts/
COPY model/count_vectorizer.pkl ./model/
COPY model/model.pkl ./model/

# Expose the port for Streamlit
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
