with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

content = content.replace("            onCloseFile = viewModel::closeFile,", "            onCloseFile = viewModel::closeFile,\n            onSaveFile = viewModel::saveFile,")

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
