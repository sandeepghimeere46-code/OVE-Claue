file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

php_desc = '''        DevStack.PHP -> "PHP sites and Laravel projects"'''
ai_desc = php_desc + '''
        DevStack.LOCAL_AI -> "Offline local AI model inference"'''

content = content.replace(php_desc, ai_desc)

with open(file_path, "w") as f:
    f.write(content)
