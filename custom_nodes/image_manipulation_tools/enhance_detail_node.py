import numpy as np
import cv2
import torch  # <- Required for image-to-tensor conversion

class EnhanceDetailNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "detail_strength": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 5.0}),
                "smoothness": ("FLOAT", {"default": 10.0, "min": 0.0, "max": 100.0}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "enhance"
    CATEGORY = "image/enhancement"

    def enhance(self, image, detail_strength, smoothness):
        results = []
        for img in image:
            if isinstance(img, torch.Tensor):
                img_np = (img.cpu().numpy() * 255).astype(np.uint8)
            else:
                img_np = (img * 255).astype(np.uint8)

            img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
            enhanced = cv2.detailEnhance(img_bgr, sigma_s=smoothness, sigma_r=detail_strength)
            enhanced_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)
            results.append(enhanced_rgb.astype(np.float32) / 255.0)

        return (torch.from_numpy(np.stack(results)).float(),)





