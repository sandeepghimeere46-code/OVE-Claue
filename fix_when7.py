file_path = "app/src/main/java/com/oveclaue/app/runtime/DshRuntimeBridge.kt"
with open(file_path, "r") as f:
    content = f.read()

bad = '''            ProviderKind.CUSTOM -> DshRoute(
                name = "mh-custom",
                keyEnv = DshRuntimeBridge.FALLBACK_KEY_ENV,
                defaultModel = model,
                custom = DshCustomRoute(profile.dshApi.ifBlank { "anthropic-messages" }, profile.resolvedBaseUrl),
            )'''

good = '''            ProviderKind.LOCAL_LLAMA -> DshRoute(
                name = "mh-local",
                keyEnv = DshRuntimeBridge.FALLBACK_KEY_ENV,
                defaultModel = model,
                custom = DshCustomRoute("openai-completions", profile.resolvedBaseUrl),
            )
            ProviderKind.CUSTOM -> DshRoute(
                name = "mh-custom",
                keyEnv = DshRuntimeBridge.FALLBACK_KEY_ENV,
                defaultModel = model,
                custom = DshCustomRoute(profile.dshApi.ifBlank { "anthropic-messages" }, profile.resolvedBaseUrl),
            )'''

content = content.replace(bad, good)

with open(file_path, "w") as f:
    f.write(content)
