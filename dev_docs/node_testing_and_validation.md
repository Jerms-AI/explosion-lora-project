🧪 Node Testing and Validation Workflow

This document outlines the testing and validation process for all custom ComfyUI nodes created in this project, including clearly defined roles for internal AI validation and developer-level verification.
✅ Goals

    Ensure each node is internally tested, debugged, and validated before being shared.

    Minimize back-and-forth and reduce friction during testing by clarifying roles.

    Catch 95%+ of bugs, shape errors, and user experience issues before handoff.

👤 Roles & Responsibilities
🤖 AI (ChatGPT) – Internal Testing & Debugging Lead

    Write and simulate the core logic of each node.

    Perform internal validation on:

        Input/output type checking

        Expected value ranges and shapes (especially for NumPy, tensors, etc.)

        Node lifecycle consistency (i.e., behavior under batch, loop, or UI refresh conditions)

    Confirm functional integration within ComfyUI:

        Validate connections to standard nodes like KSampler, Load Image, etc.

        Ensure compatibility with control types (slider, dropdown, boolean toggles)

    Handle early error-proofing:

        Provide default fallbacks for broken inputs

        Add internal try/except blocks where needed

    Ensure node works with both single and batch inputs if applicable

    Test the node in isolated cases before delivering to Jerms-AI

👨‍💻 Jerms-AI – Final Verification & Integration

    Plug the tested node into real workflows

    Verify edge cases and actual use in context:

        E.g., variations in models, samplers, conditionals

    Review naming, UX clarity, and labeling

    Confirm that node behaves as expected in different chains

    Push to GitHub once confirmed

    (Note: Your development environment runs under the system user Sunil)

🔁 Feedback Loop

If Jerms-AI finds issues:

    Only report high-level bugs or unexpected behavior.

    AI will handle debugging and refinement internally.

    Updated node will be revalidated and resubmitted.