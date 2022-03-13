from re import template
from typing import Optional
from urllib.request import Request
from fastapi import FastAPI,Request
import fastapi #fast API module
from pydantic import BaseModel #base model to define class
from fastapi.responses import HTMLResponse # to render API in HTML format {text to HTML}
from fastapi.staticfiles import StaticFiles #to access files and folders taht webpage needs
from fastapi.templating import Jinja2Templates  #to render API in HTML format {file to HTML}




app =FastAPI()

app.mount ("/static",StaticFiles(directory="static"),name="static")
templates=Jinja2Templates(directory="templates")


@app.get("/hello/{q1}")
def name(q1):
    return {"result":"sankar","UI":q1}

class CV (BaseModel):
    name:str
    age:int
    dev:bool
    hobby:Optional[list]
    
@app.post("/end2")
async def endpoint(res:CV):
    return {"username":res.name}

@app.get("/filehtml",response_class=HTMLResponse)
async def webpage(request:Request):
    return templates.TemplateResponse("index.html",context={"request":request})
