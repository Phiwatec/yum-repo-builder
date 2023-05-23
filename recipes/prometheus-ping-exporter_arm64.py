import requests
import os
import urllib.request
URL = "https://api.github.com/repos/czerwonk/ping_exporter/releases/latest"
from dotenv import load_dotenv
load_dotenv()
import os
ARCH=['amd64','arm64']
username=os.environ.get('GH_USER')
token=os.environ.get('GH_TOKEN')
auth=(username,token)


def check_version(current_version):
    resp=requests.get(URL,auth=auth)
    data=resp.json()
    new_version=data['tag_name']
    print("Current version: " + current_version)
    print("Latest version: " + new_version)
    if new_version == current_version:
        return None
    else:
        for arch in ARCH:
            for asset in data['assets']:
                if asset['name'] == f'ping_exporter_{new_version}_linux_{arch}.deb':
                   print(f'ping_exporter_{new_version}_linux_{arch}.deb')
                   return (new_version, asset['browser_download_url'],asset['name'])
            return None


def build_package(version,location):

    link=version[1]
    #print(link)
#    print(f'Location {location}')
    for arch in ARCH:
        bashCommand = f"sh ./recipes/prometheus-ping-exporter/build_{arch}.sh "+link  + " " + version[0] + " "+location+f'prometheus-ping-exporter_{version[0]}_linux_amd64.deb'+" >/tmp/deblog"
        os.system(bashCommand)
        print("Ran Bash Script")
