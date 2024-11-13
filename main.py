from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
template_engine=Jinja2Templates(directory="templates")

from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=client.notes.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    print(newDocs)
    return template_engine.TemplateResponse("index.html", {"request": request, "docs": newDocs})

@app.post("/add", response_class=RedirectResponse)
async def add_item(request: Request):
    data=await request.form()
    print(data)
    note=data["note"]
    title=data["title"]
    client.notes.notes.insert_one({"title": title, "note": note})
    return RedirectResponse(url="/", status_code=303)  # Redirect to the home page


