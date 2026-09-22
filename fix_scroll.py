with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

content = content.replace("Modifier.fillMaxSize().padding(8.dp).androidx.compose.foundation.verticalScroll(androidx.compose.foundation.rememberScrollState())", "Modifier.fillMaxSize().padding(8.dp).verticalScroll(rememberScrollState())")

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
