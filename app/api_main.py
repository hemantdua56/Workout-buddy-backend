# workout_buddy_backend/app/api_main.py

import os
import uuid
import shutil
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from app.detector import detect_equipment
from app.exercise_mapper import suggest_exercises

app = FastAPI()

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze")
async def analyze_workout(
    file: UploadFile = File(...),
    muscle: str = Form(...)
):
    try:
        temp_file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.mp4")
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        equipment = detect_equipment(temp_file_path)
        exercises = suggest_exercises(equipment, muscle)

        os.remove(temp_file_path)

        return JSONResponse({
            "equipment_detected": equipment,
            "target_muscle": muscle,
            "recommended_exercises": exercises
        })

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
