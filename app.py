from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import base64
import uvicorn


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/get_shortest_path", response_class=HTMLResponse)
def upload(request: Request, ):

    f = open("input_cases/doubleback/output.png")
    contents = f.read()
    base64_encoded_image = base64.b64encode(contents).decode("utf-8")
    return templates.TemplateResponse("display.html", {"request": request, "myImage": base64_encoded_image})


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run(app)
