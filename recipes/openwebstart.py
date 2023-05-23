import requests

import urllib.request
URL = "https://api.github.com/repos/karakun/OpenWebStart/releases/latest"
from dotenv import load_dotenv
load_dotenv()
import os

username=os.environ.get('GH_USER')
token=os.environ.get('GH_TOKEN')
auth=(username,token)


def check_version(current_version):
    resp=requests.get(URL,auth=auth)
    data=resp.json()
    new_version=data['tag_name'][1:]
    print("Current version: " + current_version)
    print("Latest version: " + new_version)
    if new_version == current_version:
        return None
    else:
        for asset in data['assets']:
            if asset['name'] == 'OpenWebStart_linux_{version}.deb'.format(version=new_version.replace('.','_')):
                return (new_version, asset['browser_download_url'],"openwebstart_{version}_amd64.deb".format(version=new_version))
        return None


def build_package(version,location):
    urllib.request.urlretrieve(version[1], location+"/"+version[2])
