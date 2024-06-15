# processing/preprocessing_functions.py
from ultralytics import YOLO 
import cv2 


modelDef = YOLO('processing/best (1).pt')

def preprocess_data_json(file_path):
    # Реализация функции предобработки данных
    imgT = cv2.imread(file_path)

    pred = modelDef(imgT, imgsz = 640)[0]

    boxes = pred.boxes.xywhn
    cls = pred.boxes.cls

    coordinates = boxes.tolist()
    classes = cls.tolist()

    # Создание списка словарей в нужном формате
    processed_data = []
    for coord, cls in zip(coordinates, classes):
        processed_data.append({
            "class": int(cls),
            "x": coord[0],
            "y": coord[1],
            "width": coord[2],
            "height": coord[3]
        })

    return processed_data