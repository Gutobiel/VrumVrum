from fastapi import FastAPI, Request, Depends, Form, status
from fastapi.templating import Jinja2Templates
from sqlalchemy import func
import uvicorn
""" import models.models """
""" from database.database import engine, sessionlocal """
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


""" models.models.Base.metadata.create_all(bind=engine) """
 
templates = Jinja2Templates(directory="templates")
 
app = FastAPI(debug=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
 
def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Tela Inicial"])
async def inicio(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})