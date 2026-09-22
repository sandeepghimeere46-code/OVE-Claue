import re

file_path = "app/src/main/java/com/oveclaue/app/runtime/RuntimeInstaller.kt"
with open(file_path, "r") as f:
    content = f.read()

# 1. Add remove logic
remove_php = '''            DevStack.PHP -> {
                aptRemove(
                    runtime.proot,
                    listOf("php-cli", "php-xml", "php-curl", "php-mbstring", "php-zip", "unzip"),
                    "Removing PHP tools",
                    onProgress,
                )
                verifyGuest(runtime.proot, "rm -f /usr/local/bin/composer", "Removing Composer")
            }'''

remove_local_ai = remove_php + '''
            DevStack.LOCAL_AI -> {
                onProgress(RuntimeInstallProgress("Removing Local AI models", 0.5f, indeterminate = true))
                verifyGuest(runtime.proot, "rm -rf /opt/local_ai /usr/local/bin/start-local-ai", "Removing Local AI files")
            }'''

content = content.replace(remove_php, remove_local_ai)

# 2. Add apply logic
apply_php = '''            DevStack.PHP -> {
                aptInstall(
                    proot,
                    listOf("php-cli", "php-xml", "php-curl", "php-mbstring", "php-zip", "unzip", "curl"),
                    "Installing PHP and common extensions",
                    from,
                    onProgress,
                )
                onProgress(RuntimeInstallProgress("Installing Composer", from + (to - from) * 0.9f))
                verifyGuest(
                    proot,
                    "curl -sS https://getcomposer.org/installer | php && mv composer.phar /usr/local/bin/composer",
                    "Composer could not be installed",
                )
            }'''

apply_local_ai = apply_php + '''
            DevStack.LOCAL_AI -> {
                onProgress(RuntimeInstallProgress("Downloading llama-server and Qwen model (~750MB)... This may take a while.", from))
                val setupScript = """
                    mkdir -p /opt/local_ai
                    cd /opt/local_ai
                    
                    if [ ! -f llama-server ]; then
                        curl -L -o llama-b3780-bin-android-arm64.zip https://github.com/ggerganov/llama.cpp/releases/download/b3780/llama-b3780-bin-android-arm64.zip
                        unzip -o llama-b3780-bin-android-arm64.zip
                        mv build/bin/llama-server .
                        chmod +x llama-server
                        rm -rf build llama-b3780-bin-android-arm64.zip
                    fi
                    
                    if [ ! -f qwen.gguf ]; then
                        curl -L -o qwen.gguf https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q8_0.gguf
                    fi
                    
                    cat << 'STARTSCRIPT' > /usr/local/bin/start-local-ai
#!/bin/bash
echo "Starting Local AI Server on port 8080..."
/opt/local_ai/llama-server -m /opt/local_ai/qwen.gguf --port 8080 --host 0.0.0.1 -c 2048 &
echo "Server started in background. You can now chat using the Local Offline AI provider."
STARTSCRIPT
                    chmod +x /usr/local/bin/start-local-ai
                """.trimIndent()
                
                verifyGuest(
                    proot,
                    setupScript,
                    "Local AI installation failed"
                )
            }'''

content = content.replace(apply_php, apply_local_ai)

with open(file_path, "w") as f:
    f.write(content)

