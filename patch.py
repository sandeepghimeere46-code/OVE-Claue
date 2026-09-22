import re

file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"

with open(file_path, "r") as f:
    content = f.read()

# 1. Add isVoiceMode state
state_declaration = '    var prompt by rememberSaveable { mutableStateOf("") }\n'
new_state = state_declaration + '    var isVoiceMode by remember { mutableStateOf(false) }\n'
content = content.replace(state_declaration, new_state)

# 2. Add VoiceInputBar block
surface_start = '''                Surface(
                    shape = RoundedCornerShape(26.dp),
                    color = MaterialTheme.colorScheme.surface,
                    border = BorderStroke('''

voice_block = '''                if (isVoiceMode) {
                    VoiceInputBar(
                        onSend = { text ->
                            isVoiceMode = false
                            onSend(text, pendingAttachments)
                            prompt = ""
                            onClearAttachments()
                        },
                        onStopToText = { text ->
                            prompt = text
                            isVoiceMode = false
                        },
                        onCancel = { isVoiceMode = false }
                    )
                } else {
                Surface(
                    shape = RoundedCornerShape(26.dp),
                    color = MaterialTheme.colorScheme.surface,
                    border = BorderStroke('''

content = content.replace(surface_start, voice_block)

# 3. Add Mic button and close the `else {` block
# The end of the Surface block is around line 4683
# First, let's insert the mic button before Spacer(Modifier.width(4.dp))
spacer_line = '                        Spacer(Modifier.width(4.dp))\n\n                        if (isRunning) {'
mic_button = '''                        IconButton(
                            onClick = { isVoiceMode = true },
                            modifier = Modifier.size(40.dp),
                            enabled = !isRunning
                        ) {
                            Icon(
                                imageVector = androidx.compose.material.icons.Icons.Default.Mic,
                                contentDescription = "Voice Input",
                                tint = MaterialTheme.colorScheme.onSurfaceVariant
                            )
                        }

                        Spacer(Modifier.width(4.dp))

                        if (isRunning) {'''
content = content.replace(spacer_line, mic_button)

# Now we need to close the `} else {` block that we opened for VoiceInputBar
# The end of the else block is where the Surface closes.
# It looks like:
#                 }
#             }
#         }
#     }
# }
# We can find the end of the `Row` and `Surface`. 

surface_end = '''                        }
                    }
                }
            }
        }
    }
}

@Composable'''

closed_surface_end = '''                        }
                    }
                }
                } // End of else block
            }
        }
    }
}

@Composable'''

content = content.replace(surface_end, closed_surface_end)

with open(file_path, "w") as f:
    f.write(content)

print("Patched PocketDevApp.kt")
