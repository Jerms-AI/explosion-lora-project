import torch
import numpy as np
import cv2

class FooterTextOverlay:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING", {
                    "default": "Sample Text",
                }),
                "footer_height": ("INT", {"default": 40, "min": 10, "max": 512}),
                "font_size": ("INT", {"default": 24, "min": 10, "max": 256}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "draw_footer"
    CATEGORY = "image/overlay"

    def draw_footer(self, image, text, footer_height, font_size):
        results = []

        for img in image:
            # Ensure we're working with a NumPy array in uint8 format
            if isinstance(img, torch.Tensor):
                img = img.cpu().numpy()
            img_np = (img * 255).clip(0, 255).astype(np.uint8)

            h, w, _ = img_np.shape
            new_h = h + footer_height

            # Create new image with space for footer
            output = np.zeros((new_h, w, 3), dtype=np.uint8)
            output[:h, :, :] = img_np

            # Draw black footer
            cv2.rectangle(output, (0, h), (w, new_h), (0, 0, 0), -1)

            # Put white text in the center
            font = cv2.FONT_HERSHEY_SIMPLEX
            text_size, _ = cv2.getTextSize(text, font, 1, 2)
            text_width = text_size[0]

            text_x = max(10, (w - text_width) // 2)
            text_y = h + (footer_height // 2) + (font_size // 2) - 5

            cv2.putText(output, text, (text_x, text_y), font, font_size / 32.0, (255, 255, 255), 2, cv2.LINE_AA)

            # Normalize back to float32 for ComfyUI
            results.append(output.astype(np.float32) / 255.0)

        return (torch.tensor(np.stack(results)),)
