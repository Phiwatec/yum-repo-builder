import json
import importlib
import os
OUTDIR = "../apt/pool/main/"
FINISH_SCRIPT = "finish.sh"
FINISH_DIR = "../apt/"
MODIFIED = False
with open('data/versions.json', 'r') as f:
    versions = json.load(f)


for filename in os.listdir("recipes/"):
    if filename.endswith(".py"):
        package_name = filename[:-3]
        mod = importlib.import_module("recipes." + package_name)
        print("Loaded recipe: " + package_name)
        if package_name in versions:
            current_version = versions[package_name]
        else:
            current_version = ""
        version, data = mod.check_version(current_version)
        if version:
            MODIFIED = True
            print("New version found, building package")
            versions[package_name] = version
            PACKAGE_PATH = os.path.join(OUTDIR, package_name)
            if not os.path.exists(PACKAGE_PATH):
                os.makedirs(PACKAGE_PATH)
            mod.build_package(version, PACKAGE_PATH+"/", data)
        else:
            print("No new version found")
if MODIFIED:
    with open('data/versions.json', 'w') as f:
        json.dump(versions, f)
    print("All packages built")
    print("Making repo")
    os.system("cd "+FINISH_DIR+"&& bash "+FINISH_SCRIPT)

    print("Done")
else:
    print('No Updates processed')
