import requests
import urllib.request

URL = "https://api.github.com/repos/smallstep/cli/releases/latest"

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
            if asset['name'] == 'step-cli_{version}_amd64.deb'.format(version=new_version):
                return (new_version, asset['browser_download_url'],asset['name'])
        return None


def build_package(version,location):
    urllib.request.urlretrieve(version[1], location+"/"+version[2])
