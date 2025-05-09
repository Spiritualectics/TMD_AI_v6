# tmd_api_v6.py – Monumental Phase 2 API
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tmd_core_v6_monumental import generate_tmd_forecast_v6
import hashlib

API_SECRET_KEY = "TMD_SECRET_KEY_2025"
API_SIGNATURE_HASH = hashlib.sha256(API_SECRET_KEY.encode()).hexdigest()

app = FastAPI(
    title="TMD-AI Monumental Forecast API",
    version="6.2",
    description="Phase 2 expansion: Full symbolic, emotional, karmic, geographic, and ancestral modeling"
)

class TMDInput(BaseModel):
    energetic_integrity: float
    emotional_instability: float
    symbolic_density: float
    spiritual_pol: str
    guilt_load: float
    dominant_emotion: str
    archetype: str
    cause_affiliation: str
    location_risk: str
    public_perception: str
    dream_symbol: str
    karmic_loop: str
    final_event_imprint: str
    api_signature: str

@app.post("/tmd-v6-forecast/")
def forecast_handler(input_data: TMDInput):
    if input_data.api_signature != API_SIGNATURE_HASH:
        raise HTTPException(status_code=401, detail="Invalid API signature. Unauthorized access.")

    forecast = generate_tmd_forecast_v6(input_data.dict())
    return {
        "status": "success",
        "author": "Badru Michael Oluwarotimi",
        "version": "v6.2",
        "forecast_result": forecast
    }
