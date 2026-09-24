import json
import os

from worlds.tloz_oos import patching

if __name__ == "__main__":
    dir_name = os.path.dirname(patching.__file__) + "/asm"
    asm_files = {}
    for filename in os.listdir(dir_name):
        if filename.endswith(".yaml"):
            asm_files["base"].append(f"asm/{filename}")
        elif filename == "disabled":
            continue
        elif filename == "conditional":
            for subfilename in os.listdir(f"{dir_name}/conditional"):
                asm_files[subfilename[:-5]] = [f"asm/conditional/{subfilename}"]
        elif "." not in filename and filename != "__pycache__":
            content = []
            for subfilename in os.listdir(f"{dir_name}/{filename}"):
                if subfilename.endswith(".yaml"):
                    content.append(f"asm/{filename}/{subfilename}")
                else:
                    for subsubfilename in os.listdir(f"{dir_name}/{filename}/{subfilename}"):
                        content.append(f"asm/{filename}/{subfilename}/{subsubfilename}")
            asm_files[filename] = content

    with open(dir_name + "/__init__.py", "w", encoding="utf-8") as f:
        f.write("asm_files = ")
        f.write(json.dumps(asm_files, indent=4))
        f.write("\n")
