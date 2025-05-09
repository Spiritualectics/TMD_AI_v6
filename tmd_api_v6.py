# ==============================================================================
# tmd_api_v6.py
# Secure FastAPI Interface for TMD-AI v6
# Author: Badru Michael Oluwarotimi
# ==============================================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
from tmd_core_v6_fufrom tmd_core_v6_full_clean import generate_tmd_forecast_v6
import hashlib

API_SECRET_KEY = "TMD_SECRET_KEY_2025"
API_SIGNATURE_HASH = hashlib.sha256(API_SECRET_KEY.encode()).hexdigest()

app = FastAPI(
    title="TMD-AI Forecast API",
    version="6.0",
    description="Terminal Manner Doctrine – AI-Powered Manner of Death Prediction Engine by Badru Michael Oluwarotimi"
)

class TMDInput(BaseModel):
    energetic_integrity: float
    emotional_instability: float
    symbolic_density: float
    spiritual_pol: Literal["Positive", "Negative", "Neutral"]
    dominant_emotion: str
    archetype: Literal["The Rebel", "The Genius", "The Servant", "The Outsider", "The Leader"]
    api_signature: str

@app.post("/tmd-v6-forecast/")
def forecast_handler(input_data: TMDInput):
    """
    Main POST endpoint to process TMD-AI forecasts.
    Validates signature, then returns TEI score, symbolic death mode predictions,
    and a description of the symbolic archetype path.
    """
    if input_data.api_signature != API_SIGNATURE_HASH:
        raise HTTPException(status_code=401, detail="Invalid API signature. Unauthorized access.")

    forecast = generate_tmd_forecast_v6(input_data.dict())
    return {
        "status": "success",
        "author": "Badru Michael Oluwarotimi",
        "version": "v6",
        "forecast_result": forecast
    }
