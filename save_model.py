import torch
import torchvision.models as models
import os

# Створення папки для збереження моделі
os.makedirs("model", exist_ok=True)

# Завантаження попередньо натренованої моделі ResNet18
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()  # Перехід у режим оцінки (inference)

# Створення "манекена" для трасування моделі
dummy_input = torch.rand(1, 3, 224, 224)

# Трасування моделі в TorchScript
traced_model = torch.jit.trace(model, dummy_input)

# Збереження моделі
traced_model.save("model/traced_model.pt")
print("✅ Model saved to model/traced_model.pt")
