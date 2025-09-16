import torch
from torchvision import transforms
from PIL import Image
import io

# Load the TorchScript model
model = torch.jit.load("model/traced_model.pt")
model.eval()

# Define preprocessing pipeline
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

# Predict from raw bytes
def predict_image(image_bytes: bytes) -> int:
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(tensor)
        return output.argmax(1).item()
