import re

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

bad_chunk = """    if (state.openedFilePath != null) {
        BackHandler(onBack = {
            onCloseFile()
                selectedTab = WorkspaceTab.FILES
            },
            onSave = { viewModel.saveFile(state.openedFilePath!!, it) }
            selectedTab = WorkspaceTab.FILES
        })"""

good_chunk = """    if (state.openedFilePath != null) {
        BackHandler(onBack = {
            viewModel.closeFile()
            selectedTab = WorkspaceTab.FILES
        })"""

content = content.replace(bad_chunk, good_chunk)

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
