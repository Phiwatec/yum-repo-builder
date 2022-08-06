import requests

import urllib.request
URL = "https://api.github.com/repos/smallstep/certificates/releases/latest"



def check_version(current_version):
    resp=requests.get(URL)
    data=resp.json()
    new_version=data['tag_name'][1:]
    print("Current version: " + current_version)
    print("Latest version: " + new_version)
    if new_version == current_version:
        return None
    else:
        for asset in data['assets']:
            if asset['name'] == 'step-ca_{version}_amd64.deb'.format(version=new_version):
                return (new_version, asset['browser_download_url'],asset['name'])
        return None


def build_package(version,location):
    urllib.request.urlretrieve(version[1], location+"/"+version[2])
