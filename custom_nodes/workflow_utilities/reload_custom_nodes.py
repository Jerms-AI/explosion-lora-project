import nodes

class ReloadCustomNodes:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}}

    RETURN_TYPES = ()
    FUNCTION = "reload"

    CATEGORY = "dev"

    def reload(self):
        nodes.reload_custom_nodes()
        print("🔁 Custom nodes reloaded.")
        return ()
