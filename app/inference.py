import sys
from app.model_utils import predict_image

if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        result = predict_image(f.read())
        print(f"🧠 Predicted class: {result}")
