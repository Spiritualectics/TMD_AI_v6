# tmd_api_v6.py – Monumental Phase 2 API with CORS and Descriptions
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from tmd_core_v6_monumental import generate_tmd_forecast_v6
import hashlib

API_SECRET_KEY = "TMD_SECRET_KEY_2025"
API_SIGNATURE_HASH = hashlib.sha256(API_SECRET_KEY.encode()).hexdigest()

app = FastAPI(
    title="TMD-AI Monumental Forecast API",
    version="6.2",
    description="Phase 2 expansion: Full symbolic, emotional, karmic, geographic, and ancestral modeling"
)

# Enable CORS so GitHub Pages can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Optionally replace "*" with ["https://spiritualectics.github.io"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class TMDInput(BaseModel):
    energetic_integrity: float = Field(..., description="Life force stability (0.0 = collapse, 5.0 = vibrant)")
    emotional_instability: float = Field(..., description="Degree of emotional chaos (0.0 = stable, 5.0 = chaotic)")
    symbolic_density: float = Field(..., description="Fate-layered significance of life events")
    spiritual_pol: str = Field(..., description="Spiritual polarity: Positive, Negative, or Neutral")
    guilt_load: float = Field(..., description="Unconscious guilt weight (0.0–5.0)")
    dominant_emotion: str = Field(..., description="Primary emotion governing subject's state")
    archetype: str = Field(..., description="Subject's symbolic identity (e.g., The Rebel, The Leader)")
    cause_affiliation: str = Field(..., description="Symbolic group connection: Political, Gang, etc.")
    location_risk: str = Field(..., description="Geographic or conflict-based risk zone")
    public_perception: str = Field(..., description="How society views the subject")
    dream_symbol: str = Field(..., description="Recurring dream or visionary motif")
    karmic_loop: str = Field(..., description="Is the subject repeating ancestral patterns? Yes/No")
    final_event_imprint: str = Field(..., description="Recent traumatic or transformative experience")
    api_signature: str = Field(..., description="Hashed API signature for secure access")

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