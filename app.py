import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

print('DB_HOST: ', bool(DB_HOST))
print('DB_PORT: ', bool(DB_PORT))
print('DB_NAME: ', bool(DB_NAME))
print('DB_USER: ', bool(DB_USER))
print('DB_PASSWORD: ', bool(DB_PASSWORD))

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}