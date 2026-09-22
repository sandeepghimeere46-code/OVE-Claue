file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

# Fix getDevStackVisuals
php_visuals = '''    DevStack.PHP -> DevStackVisuals(
        icon = Icons.Default.Dns,
        accentColor = Color(0xFF818CF8),
        tag = "php-cli + Composer",
    )'''

ai_visuals = php_visuals + '''
    DevStack.LOCAL_AI -> DevStackVisuals(
        icon = Icons.Default.Memory,
        accentColor = Color(0xFFF43F5E),
        tag = "llama-server",
    )'''
content = content.replace(php_visuals, ai_visuals)

# Need to fix line 1237
# I'll just look for DevStack.PHP -> and replace the second occurrence if there is one.
# But it's better to find the context for line 1237.
