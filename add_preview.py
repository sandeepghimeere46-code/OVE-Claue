import re

file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

# 1. Add var showPreviewSheet
state_decl = '''    var showChats by rememberSaveable { mutableStateOf(false) }'''
new_state_decl = '''    var showChats by rememberSaveable { mutableStateOf(false) }
    var showPreviewSheet by rememberSaveable { mutableStateOf(false) }'''
content = content.replace(state_decl, new_state_decl)

# 2. Add ModalBottomSheet
modal_insertion_point = '''    // If a file is open, show the FileViewerScreen on top
    if (state.openedFilePath != null) {'''
new_modal = '''    if (showPreviewSheet) {
        ModalBottomSheet(
            onDismissRequest = { showPreviewSheet = false },
            containerColor = MaterialTheme.colorScheme.background,
            modifier = Modifier.fillMaxHeight(0.85f)
        ) {
            Box(Modifier.fillMaxSize()) {
                PreviewTab(state.previewReady, state.previewUrl)
            }
        }
    }

    // If a file is open, show the FileViewerScreen on top
    if (state.openedFilePath != null) {'''
content = content.replace(modal_insertion_point, new_modal)

# 3. Add icon to TopAppBar
action_point = '''                    IconButton(onClick = { showChats = true }) { Icon(Icons.Default.History, "Project chats") }'''
new_action_point = '''                    if (state.previewReady) {
                        IconButton(onClick = { showPreviewSheet = true }) {
                            Icon(Icons.Default.Preview, "Open Web Preview", tint = PocketGreen)
                        }
                    }
                    IconButton(onClick = { showChats = true }) { Icon(Icons.Default.History, "Project chats") }'''
content = content.replace(action_point, new_action_point)

with open(file_path, "w") as f:
    f.write(content)
