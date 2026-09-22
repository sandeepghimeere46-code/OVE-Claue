import re

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

bad = """        FileViewerScreen(
            filePath = state.openedFilePath,
            content = state.openedFileContent,
            loading = state.fileContentLoading,
            onClose = {
                onCloseFile()
                selectedTab = WorkspaceTab.FILES
            },
            onSave = { viewModel.saveFile(state.openedFilePath!!, it) }
                selectedTab = WorkspaceTab.FILES
            },
        )"""

good = """        FileViewerScreen(
            filePath = state.openedFilePath,
            content = state.openedFileContent,
            loading = state.fileContentLoading,
            onClose = {
                viewModel.closeFile()
                selectedTab = WorkspaceTab.FILES
            },
            onSave = { viewModel.saveFile(state.openedFilePath!!, it) },
        )"""

if bad in content:
    content = content.replace(bad, good)
else:
    # try original
    bad2 = """        FileViewerScreen(
            filePath = state.openedFilePath,
            content = state.openedFileContent,
            loading = state.fileContentLoading,
            onClose = {
                onCloseFile()
                selectedTab = WorkspaceTab.FILES
            },
        )"""
    if bad2 in content:
        content = content.replace(bad2, good)
        print("Replaced bad2")
    else:
        print("Not found")

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
