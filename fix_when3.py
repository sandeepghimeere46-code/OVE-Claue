file_path = "app/src/main/java/com/oveclaue/app/ui/PocketDevApp.kt"
with open(file_path, "r") as f:
    content = f.read()

custom_accent = "ProviderKind.CUSTOM -> PocketOrange"
llama_accent = "ProviderKind.LOCAL_LLAMA -> Color(0xFFF43F5E)\n        " + custom_accent
content = content.replace(custom_accent, llama_accent)

custom_mark = 'ProviderKind.CUSTOM -> "<>"'
llama_mark = 'ProviderKind.LOCAL_LLAMA -> "LL"\n        ' + custom_mark
content = content.replace(custom_mark, llama_mark)

with open(file_path, "w") as f:
    f.write(content)
