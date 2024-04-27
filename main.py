from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
import os
import segno

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    file_path = "./index.html"
    with open(file_path, "r") as file:
        html_content = file.read()
    return html_content

@app.post("/qrcode")
async def get_qrcode(message: Annotated[str, Form()]):
    qrcode = segno.make_qr(message)
    qrcode.save("./assets/basic_qrcode.png", scale=5, border=10)
    file_path = "./assets/basic_qrcode.png"
    response = FileResponse(file_path)
    return response

