import re

with open("app/src/main/java/com/oveclaue/app/ui/MainViewModel.kt", "r") as f:
    content = f.read()

save_func = """
    fun saveFile(filePath: String, newContent: String) {
        val project = _state.value.activeProject ?: return
        viewModelScope.launch(Dispatchers.IO) {
            try {
                val file = java.io.File(projectWorkspaceRoot(project), filePath)
                file.writeText(newContent)
                _state.update { it.copy(openedFileContent = newContent) }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
"""

content = content.replace("fun openFile(entry: WorkspaceEntry) {", save_func + "\n    fun openFile(entry: WorkspaceEntry) {")

with open("app/src/main/java/com/oveclaue/app/ui/MainViewModel.kt", "w") as f:
    f.write(content)
