# 🧪 Workflow Utilities

This folder contains utility nodes for controlling or varying parameters in your ComfyUI workflows.

---

## 🔁 ParamSweep Node

The `ParamSweep` node takes a list of comma-separated values (e.g., `1.0, 2.0, 3.0`) and outputs them as a tensor.

### Example Use:

- Plug into any node with a FLOAT input (like `cfg`, `start_step`, `end_step`)
- ComfyUI will automatically batch over those values
- Use in combination with `TextOverlay` or save images to study output variance

More utilities coming soon!
