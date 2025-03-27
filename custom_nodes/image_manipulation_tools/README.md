# 🧰 Image Manipulation Tools - README

Welcome to the `image_manipulation_tools` node collection! This folder contains custom ComfyUI nodes designed to enhance and manipulate image outputs for both aesthetic tuning and dataset preparation.

---

## 🔍 Included Nodes

### 🎯 Enhance Detail Node

This node applies a detail enhancement filter to your images using OpenCV’s `detailEnhance` algorithm. It’s perfect for:

- Sharpening fine textures
- Making explosions pop 💥
- Enhancing details before LORA training
- ✅ Compatible with both NumPy arrays and Torch tensors

#### 🧪 Parameters:

| Parameter         | Type  | Description                                                                            |
| ----------------- | ----- | -------------------------------------------------------------------------------------- |
| `detail_strength` | Float | Controls how much detail gets emphasized. Think of this like "edge contrast."          |
| `smoothness`      | Float | Controls how smoothly those details blend into the image. Lower values = more texture. |

#### 🧠 Visual Intuition

- `detail_strength = 0.2`: Very subtle enhancement
- `detail_strength = 1.0`: Standard detail pop
- `detail_strength = 3.0+`: Very strong sharpening (can get crunchy)

- `smoothness = 5`: Gritty textures, bold lines
- `smoothness = 20`: Balanced detail with soft transitions
- `smoothness = 60+`: Gentle, almost watercolor-like detail lift

👉 *This node accepts both NumPy arrays and PyTorch tensors — and returns a Torch tensor for compatibility with all downstream ComfyUI nodes.*

---

## 🛠️ How to Use

1. Add the `Enhance Detail` node to your ComfyUI workflow
2. Connect it after your image generation node (like SDXL or Flux output)
3. Tweak `detail_strength` and `smoothness` to your taste
4. Preview the result or save to disk

💡 This is a great tool for prepping datasets intended for LoRA fine-tuning — enhance detail **before** resizing or augmentation.

---

## 📸 Example Output

> *Coming soon — before/after examples with parameter ranges.*

---

## ✍️ Author

Created by [jerms-ai](https://github.com/jerms-ai) with guidance and support from an extremely helpful co-pilot 🤖

---

## 📁 Folder Structure

```
custom_nodes/
└── image_manipulation_tools/
    ├── __init__.py
    ├── enhance_detail_node.py
    └── README.md  ← you are here
```

More nodes will be added here as the project evolves — stay tuned!

