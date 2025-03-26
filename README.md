# RAG_CSV_Analyzer

This project is a FastAPI-based service that allows users to upload, store, query, and analyze CSV files using MongoDB and a Hugging Face LLM for enhanced data analysis.

## Features

- Upload CSV files
- Store CSV data in MongoDB
- Query CSV data using string matches
- Use an LLM to answer questions based on CSV data
- API endpoints for file management and querying

## Installation

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/Tesserxt/.git
cd RAG_CSV_Analyzer
```

### 2️⃣ Create a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up MongoDB

- Ensure MongoDB is running
- Update the connection URL in `database.py`

### 5️⃣ Set your huggingFace api_key

- Ensure you have you huggingface api key
- Create api key or read token from your huggingface profile

### 6️⃣ Run the API Server

```sh
python main.py
```

The server will start at `http://127.0.0.1:8000`

## API Endpoints

### 🔹 Home

```http
GET /
```

*Returns a welcome message.*

### 🔹 Upload CSV

```http
POST /upload
```

**Input:** CSV file (multipart/form-data)\
**Output:** `{ "file_id": "string", "message": "Upload successful" }`

### 🔹 List Uploaded Files

```http
GET /files
```

**Output:** `{ "files": [{ "file_id": "string", "file_name": "string" }] }`

### 🔹 Query CSV Data

```http
POST /query
```

**Input:** `{ "file_id": "string", "query": "search term" }`

### 🔹 Query CSV Using LLM

```http
POST /query-llm
```

**Input:** `{ "file_id": "string", "query": "Ask a question about the CSV data" }`

### 🔹 Delete File

```http
DELETE /
```

**Input:** `{ "file_id": "string" }`

## Deployment

To deploy the FastAPI application using `uvicorn`, run:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

## License

This project is open-source under the MIT License.

