file_path = "app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt"
with open(file_path, "r") as f:
    content = f.read()

remove_php = '''            DevStack.PHP -> {
                aptRemove(
                    runtime.proot,
                    listOf("php-cli", "php-xml", "php-curl", "php-mbstring", "php-zip", "unzip"),
                    0.45f,
                    onProgress,
                )
                verifyGuest(runtime.proot, "rm -f /usr/local/bin/composer", "Removing Composer")
            }
        }
        writeDevStackState(readDevStackState().apply { put(stack.name, false) })'''

remove_ai = '''            DevStack.PHP -> {
                aptRemove(
                    runtime.proot,
                    listOf("php-cli", "php-xml", "php-curl", "php-mbstring", "php-zip", "unzip"),
                    0.45f,
                    onProgress,
                )
                verifyGuest(runtime.proot, "rm -f /usr/local/bin/composer", "Removing Composer")
            }
            DevStack.LOCAL_AI -> {
                verifyGuest(runtime.proot, "rm -rf /opt/local_ai /usr/local/bin/start-local-ai", "Removing Local AI")
            }
        }
        writeDevStackState(readDevStackState().apply { put(stack.name, false) })'''

content = content.replace(remove_php, remove_ai)

with open(file_path, "w") as f:
    f.write(content)
