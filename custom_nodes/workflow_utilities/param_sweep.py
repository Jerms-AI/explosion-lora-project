class ParameterSweep:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "values": ("STRING", {
                    "multiline": False,
                    "default": "1.0, 2.0, 3.0"
                })
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "sweep"
    CATEGORY = "workflow_utilities"
    BATCHABLE = True  # <- Key for automatic batching of outputs

    def sweep(self, values):
        try:
            parsed_values = [float(x.strip()) for x in values.split(",") if x.strip()]
        except ValueError:
            raise ValueError("ParameterSweep: Make sure values are comma-separated floats.")

        return (parsed_values,)
