from distutils.command.build import build
from ensurepip import version
import importlib
import os
SUBDIR="dist/"
OUTDIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),SUBDIR)
import json
with open('data/versions.json', 'r') as f:
  versions = json.load(f)



for filename in os.listdir("recipes/"):
    if filename.endswith(".py"):
        mod=importlib.import_module("recipes." + filename[:-3])
        print("Loaded recipe: " + filename[:-3])
        if filename[:-3] in versions:
            current_version = versions[filename[:-3]]
        else:
            current_version = ""
        version=mod.check_version(current_version)
        if version:
            print("New version found, building package")
            versions[filename[:-3]]=version[0]
            PACKAGE_PATH=os.path.join(OUTDIR,filename[:-3])
            if not os.path.exists(PACKAGE_PATH):
                os.makedirs(PACKAGE_PATH)
            mod.build_package(version,PACKAGE_PATH+"/")
        else:
            print("No new version found")
        
with open('data/versions.json', 'w') as f:
    json.dump(versions, f)
print("All packages built")
print("Making repo")
os.system("bash finish.sh")

print("Done")

        
        

