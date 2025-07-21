from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import calculator_router
import os
from dotenv import load_dotenv

# Load from the parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

app = FastAPI(
    title="FastAPI Calculator",
    description="A modular calculator using FastAPI.",
    version="1.0.0",
)

# CORS settings (optional but good practice)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the calculator router
app.include_router(calculator_router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Calculator"}
