from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

alerts = []  # in-memory storage (good enough for MVP)

class SOS(BaseModel):
    name: str
    msg: str
    lat: float
    lng: float
    time: str

@app.post("/sos")
def receive_sos(alert: SOS):
    alerts.append(alert.dict())
    return {"status": "received"}

@app.get("/alerts")
def get_alerts():
    return alerts

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
