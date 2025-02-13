# iNotes

A simple FastAPI app for creating and managing notes with MongoDB.

## Requirements
- Python 3.9+
- [FastAPI](https://fastapi.tiangolo.com/)
- [pymongo](https://pypi.org/project/pymongo/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- MongoDB instance or MongoDB Atlas

## Setup
1. Clone the repository:
   ```bash
   git clone (current url)
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your MongoDB connection string:
   ```bash
   MONGODB_URI="your_connection_string"
   ```

## Usage
1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Endpoints
- **GET /**  
  Renders `index.html` with an overview of existing notes.
- **POST /add**  
  Accepts form data with `"title"` and `"note"`, then stores them in MongoDB, returning a redirect to the main page.

## Project Structure
- `main.py` – FastAPI application  
- `templates/` – HTML templates  
- `static/` – Static files (CSS, JS)  
- `.env` – Environment variables (MongoDB URI)  

Contributions and suggestions are welcome.
```