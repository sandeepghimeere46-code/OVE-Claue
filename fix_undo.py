file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

closed_surface_end = '''                        }
                    }
                }
                } // End of else block
            }
        }
    }
}

@Composable'''

surface_end = '''                        }
                    }
                }
            }
        }
    }
}

@Composable'''

content = content.replace(closed_surface_end, surface_end)
with open(file_path, "w") as f:
    f.write(content)
