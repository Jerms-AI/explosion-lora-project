# Placeholder for README.md# 💣 Explosion LORA Project

This repo documents a hands-on journey into training a custom LoRA (Low-Rank Adaptation) for explosions, using ComfyUI with SDXL and Flux models, plus custom enhancement nodes built from scratch.

---

## 🚀 Project Structure

```
explosion-lora-project/
├── custom_nodes/
│   └── image_manipulation_tools/
│       ├── __init__.py
│       ├── enhance_detail_node.py
│       └── README.md   ← Docs for Enhance Detail Node ✅
├── comfyui_workflows/
│   └── explosion_generation.json
├── training/
│   └── train_lora_sdxl.py
├── .gitignore
├── README.md  ← You are here
└── requirements.txt
```

---

## 🧠 Custom Nodes

We’re extending ComfyUI with simple but powerful image processing tools. Currently includes:

### 🔹 [Enhance Detail Node](custom_nodes/image_manipulation_tools/README.md)
> Boost image detail using OpenCV's `detailEnhance`. Tweak contrast, texture, and clarity before dataset generation or final renders.

More nodes coming soon (contrast, blur, mask tweaks, etc). Each one will live in its own modular Python file with docs.

---

## 🧪 Dataset Creation Workflows

Inside `comfyui_workflows/explosion_generation.json`, you'll find a node-based image creation pipeline combining:
- SDXL + Flux fusion
- Custom enhancement passes
- High-quality explosion image generation

This is experimental and will be refactored as the project progresses.

---

## 🎯 Training

The `training/train_lora_sdxl.py` script will eventually contain a clean LoRA fine-tuning workflow using 🤗 diffusers or direct PyTorch.

We're bypassing GUI tools like `kohya_ss` for full control.

---

## 👤 Author
Created by [jerms-ai](https://github.com/jerms-ai)

Project purpose: To create powerful aesthetic datasets, learn fine-tuning techniques, and show off technical artistry with custom ComfyUI tooling.

---

## 📸 Demo Images
Coming soon...

Want to contribute or follow along? Watch this space — or fork and start enhancing your own images!

