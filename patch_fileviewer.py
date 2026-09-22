import re

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

pattern = re.compile(r"else -> \{\s*// Code / plain-text viewer.*?\}\s*\}\s*\}\s*\}", re.DOTALL)

new_editor = """else -> {
                    // Code Editor
                    var editMode by remember { mutableStateOf(false) }
                    var draftContent by remember(content) { mutableStateOf(content) }
                    
                    Column(Modifier.fillMaxSize().background(Color(0xFF0D1117))) {
                        Row(Modifier.fillMaxWidth().background(Color(0xFF161B22)).padding(8.dp), horizontalArrangement = Arrangement.End) {
                            if (editMode) {
                                TextButton(onClick = { editMode = false; draftContent = content }) {
                                    Text("Cancel", color = Color(0xFF8B949E))
                                }
                                OutlinedButton(onClick = { onSave(draftContent); editMode = false }) {
                                    Text("Save Changes", color = Color(0xFFE27B40))
                                }
                            } else {
                                OutlinedButton(onClick = { editMode = true }) {
                                    Text("Edit Code", color = Color(0xFFE27B40))
                                }
                            }
                        }
                        
                        Box(Modifier.fillMaxSize()) {
                            if (editMode) {
                                BasicTextField(
                                    value = draftContent,
                                    onValueChange = { draftContent = it },
                                    modifier = Modifier.fillMaxSize().padding(8.dp).androidx.compose.foundation.verticalScroll(androidx.compose.foundation.rememberScrollState()),
                                    textStyle = TextStyle(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 13.sp,
                                        color = Color(0xFFC9D1D9)
                                    ),
                                    cursorBrush = SolidColor(Color(0xFFE27B40))
                                )
                            } else {
                                BasicTextField(
                                    value = content,
                                    onValueChange = {},
                                    readOnly = true,
                                    modifier = Modifier.fillMaxSize().padding(8.dp).androidx.compose.foundation.verticalScroll(androidx.compose.foundation.rememberScrollState()),
                                    textStyle = TextStyle(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 13.sp,
                                        color = Color(0xFFC9D1D9)
                                    ),
                                    cursorBrush = SolidColor(Color.Transparent)
                                )
                            }
                        }
                    }
                }
            }
        }
    }"""

content = pattern.sub(new_editor, content, count=1)

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
