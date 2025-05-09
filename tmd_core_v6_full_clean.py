# tmd_core_v6_full.py
# Terminal Manner Doctrine AI Core – v6 (Deployable Edition)
# Author: Badru Michael Oluwarotimi

def compute_tei(energetic_integrity, emotional_instability, symbolic_density, spiritual_pol):
    polarity_score = 1 if spiritual_pol == "Positive" else -1 if spiritual_pol == "Negative" else 0
    tei = (
        (energetic_integrity * 0.4) +
        (symbolic_density * 0.2) -
        (emotional_instability * 0.3) +
        (polarity_score * 0.1)
    )
    return round(tei, 2)

def interpret_death_modes(tei, dominant_emotion, archetype):
    death_modes = {}

    if tei < 2.0:
        death_modes["Energetic Collapse"] = 80
        death_modes["Psychospiritual Exhaustion"] = 65
        death_modes["Symbolic Death"] = 50
    elif tei < 3.0:
        death_modes["Dissonant Burnout"] = 60
        death_modes["Karmic Discharge"] = 50
    else:
        death_modes["Stability Sustained"] = 75
        death_modes["Evolutionary Extension"] = 65

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
        data["energetic_integrity"],
        data["emotional_instability"],
        data["symbolic_density"],
        data["spiritual_pol"]
    )
    death_modes = interpret_death_modes(tei, data["dominant_emotion"], data["archetype"])
    symbolic_role = describe_symbolic_role(data["archetype"])
    return {
        "TEI_Score": tei,
        "Death_Mode_Predictions": death_modes,
        "Symbolic_Archetype_Description": symbolic_role
    }