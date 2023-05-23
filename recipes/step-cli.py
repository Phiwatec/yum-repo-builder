import os
from dotenv import load_dotenv
import requests
import urllib.request

URL = "https://api.github.com/repos/smallstep/cli/releases/latest"

load_dotenv()

username = os.environ.get('GH_USER')
token = os.environ.get('GH_TOKEN')
auth = (username, token)


def check_version(current_version):
    resp = requests.get(URL, auth=auth)
    data = resp.json()
    new_version = data['tag_name'][1:]
    print("Current version: " + current_version)
    print("Latest version: " + new_version)
    if new_version == current_version:
        return (None, None)
    else:
        for asset in data['assets']:
            if asset['name'] == f'step-cli_{new_version}_amd64.deb':
                return (new_version, (asset['browser_download_url'], asset['name']))
        return (None, None)


def build_package(version, location, data):
    urllib.request.urlretrieve(data[0], location+"/"+data[1])
