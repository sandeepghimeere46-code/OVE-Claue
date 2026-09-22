with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

content = content.replace("    onCloseFile: () -> Unit,", "    onCloseFile: () -> Unit,\n    onSaveFile: (String, String) -> Unit,")

content = content.replace("viewModel.closeFile()", "onCloseFile()")
content = content.replace("viewModel.saveFile(state.openedFilePath!!, it)", "onSaveFile(state.openedFilePath!!, it)")

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
