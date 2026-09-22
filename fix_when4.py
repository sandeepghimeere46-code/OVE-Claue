import re

# DshRuntimeBridge.kt
file_path_dsh = "app/src/main/java/com/oveclaue/app/runtime/DshRuntimeBridge.kt"
with open(file_path_dsh, "r") as f:
    content = f.read()

custom = '''            ProviderKind.CUSTOM -> DshRoute(
                name = "mh-custom",
                keyEnv = DshRuntimeBridge.FALLBACK_KEY_ENV,
                defaultModel = model,
                custom = DshCustomRoute(profile.dshApi, profile.resolvedBaseUrl),
            )
        }'''

llama = '''            ProviderKind.LOCAL_LLAMA -> DshRoute(
                name = "mh-local",
                keyEnv = DshRuntimeBridge.FALLBACK_KEY_ENV,
                defaultModel = model,
                custom = DshCustomRoute(profile.dshApi, profile.resolvedBaseUrl),
            )
            ProviderKind.CUSTOM -> DshRoute(
                name = "mh-custom",
                keyEnv = DshRuntimeBridge.FALLBACK_KEY_ENV,
                defaultModel = model,
                custom = DshCustomRoute(profile.dshApi, profile.resolvedBaseUrl),
            )
        }'''

content = content.replace(custom, llama)
with open(file_path_dsh, "w") as f:
    f.write(content)

# RuntimeInstaller.kt
file_path_ri = "app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt"
with open(file_path_ri, "r") as f:
    content_ri = f.read()

# I patched RuntimeInstaller previously, but it seems I might have messed up or they were restored.
# Oh, the error says:
# e: file:///workspace/nimble-ramanujan/OVE-Claue/app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt:655:9 'when' expression must be exhaustive. Add the 'LOCAL_AI' branch or an 'else' branch.
# e: file:///workspace/nimble-ramanujan/OVE-Claue/app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt:751:9 'when' expression must be exhaustive. Add the 'LOCAL_AI' branch or an 'else' branch.

# Wait, I didn't see LOCAL_AI in RuntimeInstaller.kt in the diff earlier? I think the patch script `patch_installer.py` failed silently because it didn't find the exact match string! 
