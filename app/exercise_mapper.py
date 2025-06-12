# workout_buddy_backend/app/exercise_mapper.py

def suggest_exercises(equipment: list, muscle: str) -> list:
    # Simple rule-based suggestion logic
    db = {
        "chest": {
            "bench": ["bench press", "incline bench press"],
            "dumbbell": ["dumbbell fly", "dumbbell press"],
            "barbell": ["barbell bench press"]
        },
        "legs": {
            "barbell": ["squats"],
            "dumbbell": ["lunges", "goblet squat"]
        },
        "back": {
            "barbell": ["barbell row"],
            "dumbbell": ["single arm row"]
        }
    }

    suggestions = set()
    for gear in equipment:
        suggestions.update(db.get(muscle, {}).get(gear, []))

    return list(suggestions) if suggestions else ["No suggestions available"]
