file_path = "app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt"
with open(file_path, "r") as f:
    content = f.read()

bad = '''            DevStack.PHP -> {
                aptRemove(
                    runtime.proot,
                    listOf("php-cli", "php-mbstring", "php-xml", "php-curl", "php-zip"),
                    0.45f,
                    onProgress,
                )
                removePath(File(rootfs, "usr/local/bin/composer"))
                removePath(File(rootfs, "root/.cache/composer"))
                removePath(File(rootfs, "root/.composer"))
            }
        }'''

good = '''            DevStack.PHP -> {
                aptRemove(
                    runtime.proot,
                    listOf("php-cli", "php-mbstring", "php-xml", "php-curl", "php-zip"),
                    0.45f,
                    onProgress,
                )
                removePath(File(rootfs, "usr/local/bin/composer"))
                removePath(File(rootfs, "root/.cache/composer"))
                removePath(File(rootfs, "root/.composer"))
            }
            DevStack.LOCAL_AI -> {
                verifyGuest(runtime.proot, "rm -rf /opt/local_ai /usr/local/bin/start-local-ai", "Removing Local AI")
            }
        }'''

content = content.replace(bad, good)
with open(file_path, "w") as f:
    f.write(content)
