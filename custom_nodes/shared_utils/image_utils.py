import numpy as np
import torch
from PIL import Image

def ensure_numpy(image):
    """Convert torch tensor or nested tensor to NumPy."""
    if isinstance(image, list):
        image = image[0]
    if isinstance(image, torch.Tensor):
        image = image.cpu().numpy()
    if isinstance(image, np.ndarray):
        while image.ndim > 3:
            image = np.squeeze(image, axis=0)
    return image

def numpy_to_pil(image):
    """Convert numpy array to PIL RGBA image."""
    image = ensure_numpy(image)

    # Squeeze singleton dimensions
    while image.ndim > 3:
        image = np.squeeze(image, axis=0)

    if image.ndim == 2:
        image = np.stack([image] * 3, axis=-1)
    elif image.ndim == 3 and image.shape[-1] == 1:
        image = np.repeat(image, 3, axis=-1)

    if image.dtype in [np.float32, np.float64]:
        image = np.clip(image * 255.0, 0, 255).astype(np.uint8)
    elif image.dtype != np.uint8:
        image = image.astype(np.uint8)

    return Image.fromarray(image).convert("RGBA")

def pil_to_numpy(image):
    """Convert PIL image to float32 NumPy RGB array scaled to [0, 1]."""
    return np.array(image.convert("RGB")).astype(np.float32) / 255.0

def pil_to_tensor(image):
    """Convert PIL image to PyTorch tensor scaled to [0, 1]."""
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).permute(2, 0, 1)
