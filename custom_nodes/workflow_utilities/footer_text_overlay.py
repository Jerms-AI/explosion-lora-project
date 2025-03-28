import sys
import os

# Add the full shared_utils path directly to sys.path
SHARED_UTILS_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "shared_utils")
)

if SHARED_UTILS_PATH not in sys.path:
    sys.path.insert(0, SHARED_UTILS_PATH)

from image_utils import ensure_numpy, numpy_to_pil, pil_to_tensor
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class FooterTextOverlay:
    def __init__(self):
        # System font (cross-platform fallback)
        self.font_path = "arial.ttf"
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
        image = numpy_to_pil(ensure_numpy(image))
        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
        except OSError:
            font = ImageFont.load_default()

        draw = ImageDraw.Draw(image)
        max_text_width = image.width - (2 * self.padding_sides)

        # Manual text wrap
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

        footer = Image.new("RGBA", (image.width, footer_height), (0, 0, 0, 255))
        footer_draw = ImageDraw.Draw(footer)

        y = self.padding_top
        for line in lines:
            footer_draw.text((self.padding_sides, y), line, font=font, fill=(255, 255, 255, 255))
            y += line_height

        combined = Image.new("RGBA", (image.width, image.height + footer.height))
        combined.paste(image, (0, 0))
        combined.paste(footer, (0, image.height))

        return (pil_to_tensor(combined),)
