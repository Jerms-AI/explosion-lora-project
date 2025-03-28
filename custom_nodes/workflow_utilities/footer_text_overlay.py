import os
import sys
import numpy as np
import torch
from PIL import Image, ImageDraw, ImageFont

# Add shared_utils to sys.path for local imports
SHARED_UTILS_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "shared_utils")
)
if SHARED_UTILS_PATH not in sys.path:
    sys.path.insert(0, SHARED_UTILS_PATH)

from image_utils import ensure_numpy, numpy_to_pil, pil_to_tensor

class FooterTextOverlay:
    def __init__(self):
        self.font_path = None  # Use default font
        self.font_size = 24
        self.padding_top = 20
        self.padding_bottom = 20
        self.padding_sides = 10

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "text": ("STRING", {"multiline": True}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "add_footer"
    CATEGORY = "image/text"

    def add_footer(self, image, text):
        image_np = ensure_numpy(image)
        image_pil = numpy_to_pil(image_np)

        try:
            font = ImageFont.truetype("arial.ttf", self.font_size)
        except OSError:
            font = ImageFont.load_default()

        draw = ImageDraw.Draw(image_pil)
        max_text_width = image_pil.width - (2 * self.padding_sides)

        # Word wrapping
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            test_line = f"{current_line} {word}".strip()
            if draw.textlength(test_line, font=font) <= max_text_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        line_height = font.getbbox("A")[3] - font.getbbox("A")[1]
        text_height = len(lines) * line_height

        footer_height = text_height + self.padding_top + self.padding_bottom
        footer = Image.new("RGBA", (image_pil.width, footer_height), (0, 0, 0, 255))
        footer_draw = ImageDraw.Draw(footer)

        y = self.padding_top
        for line in lines:
            footer_draw.text((self.padding_sides, y), line, font=font, fill=(255, 255, 255, 255))
            y += line_height

        combined = Image.new("RGBA", (image_pil.width, image_pil.height + footer.height))
        combined.paste(image_pil.convert("RGBA"), (0, 0))
        combined.paste(footer, (0, image_pil.height))

        return (pil_to_tensor(combined),)


NODE_CLASS_MAPPINGS = {
    "FooterTextOverlay": FooterTextOverlay
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FooterTextOverlay": "Footer Text Overlay"
}
