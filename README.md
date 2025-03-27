# 💣 Explosion LORA Project

This repo documents a hands-on journey into training a custom LoRA (Low-Rank Adaptation) for explosions, using ComfyUI with a **creatively merged SDXL model** and Flux models, plus custom enhancement nodes built from scratch.

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
Boost image detail using OpenCV’s `detailEnhance`.  
This node:
- Handles both NumPy arrays and PyTorch tensors
- Outputs a tensor for seamless ComfyUI integration
- Lets you tweak `detail_strength` and `smoothness` to control clarity and texture

Use it before training LoRA datasets or final renders to sharpen image fidelity.

More nodes coming soon (contrast, blur, mask tweaks, etc). Each one will live in its own modular Python file with docs.

---

## 🧪 Dataset Creation Workflows

Inside `comfyui_workflows/explosion_generation.json`, you'll find a node-based image creation pipeline combining:
- A creatively merged SDXL model + Flux fusion
- Custom enhancement passes
- High-quality explosion image generation

This is experimental and will be refactored as the project progresses.

---

## 🎯 Training

The `training/train_lora_sdxl.py` script will eventually contain a clean LoRA fine-tuning workflow using 🤗 diffusers or direct PyTorch.

We're bypassing GUI tools like `kohya_ss` for full control.

---

## 🧾 Dataset Creation Guidelines

### 📏 Resolution Tips
- **Generate high-res images** (e.g. 2048x2048) to retain visual clarity
- **Crop or resize** to 1024x1024 (or 896x896) for training — especially for SDXL
- Use full-res versions for showcasing or post-training super-resolution

### 🎨 Diversity for Smarter Models
Introduce variety in:
- **Composition**: close-ups, wide shots, centered, off-angle
- **Lighting**: natural, cinematic, backlit, moody
- **Color grading**: warm explosions, cool explosions, desaturated
- **Environment**: explosions in urban, forest, desert, water, sci-fi
- **Style**: hyperrealistic, painterly, vintage, surreal

### 📱 Vertical Framing Consideration
For social platforms (Instagram, TikTok, etc.):
- 9:16 aspect ratio (e.g. 1056x1888) looks great on mobile
- Nodes like *Flux Resolution Calc* can assist with intelligent cropping
- Output at 2K and downscale to 9:16 as needed for punchy visuals

The goal is to capture the aesthetic *and* functional diversity that teaches your model how to generalize — not just memorize.

---

## 👤 Author
Created by [jerms-ai](https://github.com/jerms-ai)

Project purpose: To create powerful aesthetic datasets, learn fine-tuning techniques, and show off technical artistry with custom ComfyUI tooling.

---

## 📸 Demo Images
Coming soon...

Want to contribute or follow along? Watch this space — or fork and start enhancing your own images!

