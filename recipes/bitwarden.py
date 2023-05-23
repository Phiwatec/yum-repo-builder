import requests

import urllib.request
URL = "https://api.github.com/repos/bitwarden/clients/releases"
from dotenv import load_dotenv
load_dotenv()
import os

username=os.environ.get('GH_USER')
token=os.environ.get('GH_TOKEN')
auth=(username,token)

def check_version(current_version):
    resp=requests.get(URL,auth=auth)
    data=resp.json()
    for release in data:
       if 'desktop' in release['tag_name']:
          new_version=release['tag_name']
          asset_url=release['assets_url']
          break
    #new_version=data['tag_name'][1:]
    print("Current version: " + current_version)
    print("Latest version: " + new_version)
    if new_version == current_version:
        return None
    else:
        resp=requests.get(asset_url,auth=auth)
        asset_data=resp.json()
       # print(asset_data)
        for asset in asset_data:
            if '.deb' in asset['name'] :
                return (new_version, asset['browser_download_url'],asset['name'])
        return None


def build_package(version,location):
    #return
    print(version)
    print(location)
    urllib.request.urlretrieve(version[1], location+"/"+version[2])


if __name__ == "__main__":
   check_version('')
   build_package('','')
