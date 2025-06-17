def analyze_emotion(note: str) -> dict:
    """
    Analyse basique (mock) d'une émotion.
    """
    note_lower = note.lower()
    if "triste" in note_lower:
        return {"emotion": "tristesse", "intensity": 4}
    elif "heureux" in note_lower or "joie" in note_lower:
        return {"emotion": "joie", "intensity": 5}
    elif "stress" in note_lower:
        return {"emotion": "stress", "intensity": 3}
    else:
        return {"emotion": "neutre", "intensity": 2}