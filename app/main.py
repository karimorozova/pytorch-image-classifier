from fastapi import FastAPI, File, UploadFile
from app.model_utils import predict_image

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ML inference API is ready 🎉"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    class_id = predict_image(image_bytes)
    return {"predicted_class": class_id}
