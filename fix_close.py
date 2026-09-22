file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

target = '''                                    modifier = Modifier.size(19.dp),
                                )
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable
private fun LiveClaudeProcess('''

replacement = '''                                    modifier = Modifier.size(19.dp),
                                )
                            }
                        }
                    }
                }
                }
            }
        }
    }
}

@Composable
private fun LiveClaudeProcess('''

content = content.replace(target, replacement)
with open(file_path, "w") as f:
    f.write(content)
