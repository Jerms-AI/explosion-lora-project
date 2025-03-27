# 🌀 Development Cycle

Our iterative build philosophy follows a fast-paced, feedback-driven cycle:

## 🔁 Cycle Phases
1. **Ideate** — Come up with a useful node or workflow improvement.
2. **Scaffold** — Create the file structure, folders, and base class.
3. **Build** — Implement the core functionality.
4. **Test** — Use internal validation, mock data, and catch errors early.
5. **Refine** — Fix bugs, improve performance, and polish UI.
6. **Document** — Write README, usage examples, and include visuals.
7. **Push** — Add to GitHub with meaningful commit messages.
8. **Showcase** — Use the tool in a workflow, screenshot the results, and share it.

## 🔧 Tooling
- Symlink workflow folders to avoid duplication
- Separate development and production ComfyUI folders
- Use isolated test images and tensors
- Hot reloading when possible

## ✅ Guidelines
- Keep naming clear (`snake_case`)
- Use one `.py` file per node unless tightly related
- Document assumptions inside the node

