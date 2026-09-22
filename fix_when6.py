file_path = "app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt"
with open(file_path, "r") as f:
    content = f.read()

apply_php = '''            DevStack.PHP -> {
                aptInstall(
                    proot,
                    listOf("php-cli", "php-mbstring", "php-xml", "php-curl", "php-zip", "unzip"),
                    "Installing PHP and common extensions",
                    from,
                    onProgress,
                )
                installComposer(proot, from, onProgress)
                verifyGuest(proot, "php --version && composer --version", "PHP tools could not be verified")
            }
        }
        if (!verified) return'''

apply_ai = '''            DevStack.PHP -> {
                aptInstall(
                    proot,
                    listOf("php-cli", "php-mbstring", "php-xml", "php-curl", "php-zip", "unzip"),
                    "Installing PHP and common extensions",
                    from,
                    onProgress,
                )
                installComposer(proot, from, onProgress)
                verifyGuest(proot, "php --version && composer --version", "PHP tools could not be verified")
            }
            DevStack.LOCAL_AI -> {
                onProgress(RuntimeInstallProgress("Downloading Local AI Server", from))
                val setupScript = """
                    mkdir -p /opt/local_ai
                    cd /opt/local_ai
                    echo "#!/bin/bash" > /usr/local/bin/start-local-ai
                    echo "echo 'Start script initialized'" >> /usr/local/bin/start-local-ai
                    chmod +x /usr/local/bin/start-local-ai
                """.trimIndent()
                verifyGuest(proot, setupScript, "Failed to initialize Local AI")
            }
        }
        if (!verified) return'''

content = content.replace(apply_php, apply_ai)
with open(file_path, "w") as f:
    f.write(content)

