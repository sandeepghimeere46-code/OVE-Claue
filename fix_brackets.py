with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

bad_brackets = """                                    cursorBrush = SolidColor(Color.Transparent),
                                    visualTransformation = SyntaxHighlighter()
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
    }
}

@Composable"""

good_brackets = """                                    cursorBrush = SolidColor(Color.Transparent),
                                    visualTransformation = SyntaxHighlighter()
                                )
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable"""

content = content.replace(bad_brackets, good_brackets)

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
