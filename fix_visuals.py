file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

bad = """    DevStack.PHP -> DevStackVisuals(
        icon = Icons.Default.Dns,
        accentColor = Color(0xFF818CF8),
        tag = "php-cli + Composer",
    )
    DevStack.LOCAL_AI -> DevStackVisuals(
        icon = Icons.Default.Memory,
        accentColor = Color(0xFFF43F5E),
        tag = "llama-server",
    )
    )"""

good = """    DevStack.PHP -> DevStackVisuals(
        icon = Icons.Default.Dns,
        accentColor = Color(0xFF818CF8),
        tag = "php-cli + Composer",
    )
    DevStack.LOCAL_AI -> DevStackVisuals(
        icon = Icons.Default.Memory,
        accentColor = Color(0xFFF43F5E),
        tag = "llama-server",
    )"""
content = content.replace(bad, good)
with open(file_path, "w") as f:
    f.write(content)
