file_path = "app/build.gradle.kts"
with open(file_path, "r") as f:
    content = f.read()

bad = '''    //externalNativeBuild {
    //    cmake {
    //        path = file("src/main/cpp/CMakeLists.txt")
    //    }
    //}'''
good = '''    externalNativeBuild {
        cmake {
            path = file("src/main/cpp/CMakeLists.txt")
        }
    }'''
content = content.replace(bad, good)
with open(file_path, "w") as f:
    f.write(content)
