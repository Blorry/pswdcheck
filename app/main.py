from fastapi import FastAPI
from pydantic import BaseModel

from app.strength import check, generate

app = FastAPI(title="Password Strength API")


class PasswordIn(BaseModel):
    password: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/check")
def check_password(payload: PasswordIn):
    return check(payload.password)


@app.get("/generate")
def generate_password(length: int = 16):
    length = max(8, min(length, 128))
    pw = generate(length)
    return {"password": pw, **check(pw)}
