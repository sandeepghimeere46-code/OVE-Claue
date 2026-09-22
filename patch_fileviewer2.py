import re

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "r") as f:
    content = f.read()

bad1 = """                                    textStyle = TextStyle(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 13.sp,
                                        color = Color(0xFFC9D1D9)
                                    ),
                                    cursorBrush = SolidColor(Color(0xFFE27B40))
                                )"""

good1 = """                                    textStyle = TextStyle(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 13.sp,
                                        color = Color(0xFFC9D1D9)
                                    ),
                                    cursorBrush = SolidColor(Color(0xFFE27B40)),
                                    visualTransformation = SyntaxHighlighter()
                                )"""

bad2 = """                                    textStyle = TextStyle(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 13.sp,
                                        color = Color(0xFFC9D1D9)
                                    ),
                                    cursorBrush = SolidColor(Color.Transparent)
                                )"""

good2 = """                                    textStyle = TextStyle(
                                        fontFamily = FontFamily.Monospace,
                                        fontSize = 13.sp,
                                        color = Color(0xFFC9D1D9)
                                    ),
                                    cursorBrush = SolidColor(Color.Transparent),
                                    visualTransformation = SyntaxHighlighter()
                                )"""

content = content.replace(bad1, good1).replace(bad2, good2)

with open("app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt", "w") as f:
    f.write(content)
