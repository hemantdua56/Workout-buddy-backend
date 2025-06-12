# workout_buddy_backend/app/detector.py

from ultralytics import YOLO
import cv2

def detect_equipment(video_path: str) -> list:
    model = YOLO("yolov8n.pt")  # Lightweight model; use yolov8s.pt or custom model for more accuracy
    cap = cv2.VideoCapture(video_path)

    equipment_detected = set()
    frame_count = 0
    max_frames = 5  # To reduce compute, limit analysis to first 5 frames

    while cap.isOpened() and frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for result in results:
            for cls_id in result.boxes.cls.tolist():
                class_name = result.names[int(cls_id)]
                if class_name in ["dumbbell", "barbell", "bench", "kettlebell"]:
                    equipment_detected.add(class_name)

        frame_count += 1

    cap.release()
    return list(equipment_detected) if equipment_detected else ["no_equipment_found"]
