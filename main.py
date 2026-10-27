from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from data import portfolio_data, project_data

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Zelote Portfolio", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "portfolio": portfolio_data, "projects": project_data},
    )


@app.get("/api/portfolio")
async def get_portfolio():
    return portfolio_data


@app.get("/api/projects")
async def get_projects():
    return {"projects": project_data}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
