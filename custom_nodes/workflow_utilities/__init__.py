from .param_sweep import ParameterSweep
from .reload_custom_nodes import ReloadCustomNodes
from .footer_text_overlay import FooterTextOverlay

NODE_CLASS_MAPPINGS = {
    "ParameterSweep": ParameterSweep,
    "ReloadCustomNodes": ReloadCustomNodes,
    "FooterTextOverlay": FooterTextOverlay,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ParameterSweep": "Parameter Sweep",
    "ReloadCustomNodes": "Reload Custom Nodes",
    "FooterTextOverlay": "Footer Text Overlay",
}
