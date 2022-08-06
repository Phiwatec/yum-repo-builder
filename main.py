from distutils.command.build import build
from ensurepip import version
import importlib
import os
OUTDIR=os.path.join(os.path.dirname(os.path.abspath(__file__)),'dist')
import json
with open('data/versions.json', 'r') as f:
  versions = json.load(f)



for filename in os.listdir("recipes/"):
    if filename. endswith(".py"):
        mod=importlib.import_module("recipes." + filename[:-3])
        print("Loaded recipe: " + filename[:-3])
        current_version = versions[filename[:-3]]
        version=mod.check_version(current_version)
        if version:
            print("New version found, building package")
            versions[filename[:-3]]=version[0]
            mod.build_package(version,OUTDIR)
        else:
            print("No new version found")
        
with open('data/versions.json', 'w') as f:
    json.dump(versions, f)
print("All packages built")
print("Making repo")
os.system("bash finish.sh")

print("Done")

        
        

