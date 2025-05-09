# tmd_core_v6_monumental.py – Full Expanded Engine

def compute_tei(energetic_integrity, emotional_instability, symbolic_density, spiritual_pol, guilt_load, karmic_loop):
    polarity_score = 1 if spiritual_pol == "Positive" else -1 if spiritual_pol == "Negative" else 0
    guilt_penalty = guilt_load * 0.2
    karmic_penalty = 0.5 if karmic_loop == "Yes" else 0

    tei = (
        (energetic_integrity * 0.4) +
        (symbolic_density * 0.2) -
        (emotional_instability * 0.3) -
        guilt_penalty -
        karmic_penalty +
        (polarity_score * 0.1)
    )
    return round(tei, 2)

def interpret_death_modes(tei, archetype, cause_affiliation, location_risk, public_perception, dream_symbol):
    death_modes = {}

    risk_score = 0
    if cause_affiliation in ["Political", "Gang/Street Identity", "Military/Insurgency"]:
        risk_score += 10
    if location_risk in ["Conflict Zone", "High-Crime Urban Area", "Politically Unstable Region"]:
        risk_score += 10
    if public_perception in ["Vilified", "Erased"]:
        risk_score += 5
    if dream_symbol in ["Blood", "Burial", "Falling", "Otherworldly Voice"]:
        risk_score += 7

    if tei < 2.0:
        death_modes["Energetic Collapse"] = 80 + risk_score
        death_modes["Psychospiritual Exhaustion"] = 65 + int(risk_score * 0.5)
        death_modes["Symbolic Death"] = 55 + int(risk_score * 0.6)
    elif tei < 3.0:
        death_modes["Dissonant Burnout"] = 60 + int(risk_score * 0.5)
        death_modes["Karmic Discharge"] = 50 + int(risk_score * 0.4)
    else:
        death_modes["Stability Sustained"] = 75 - int(risk_score * 0.3)
        death_modes["Evolutionary Extension"] = 65 - int(risk_score * 0.2)

    return death_modes

def describe_symbolic_role(archetype):
    roles = {
        "The Rebel": "Martyrdom or symbolic revolt.",
        "The Genius": "Misunderstood implosion.",
        "The Servant": "Burnout from sacrifice.",
        "The Outsider": "Energetic fading or erasure.",
        "The Leader": "Collapse from karmic weight."
    }
    return roles.get(archetype, "Unknown archetype")

def generate_tmd_forecast_v6(data):
    tei = compute_tei(
        float(data["energetic_integrity"]),
        float(data["emotional_instability"]),
        float(data["symbolic_density"]),
        data["spiritual_pol"],
        float(data["guilt_load"]),
        data["karmic_loop"]
    )

    death_modes = interpret_death_modes(
        tei,
        data["archetype"],
        data["cause_affiliation"],
        data["location_risk"],
        data["public_perception"],
        data["dream_symbol"]
    )

    symbolic_role = describe_symbolic_role(data["archetype"])

    return {
        "TEI_Score": tei,
        "Death_Mode_Predictions": death_modes,
        "Symbolic_Archetype_Description": symbolic_role
    }