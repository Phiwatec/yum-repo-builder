from dotenv import load_dotenv
import requests
import os
import urllib.request
URL = "https://api.github.com/repos/czerwonk/ping_exporter/releases/latest"
load_dotenv()
ARCH = ['amd64', 'arm64']
username = os.environ.get('GH_USER')
token = os.environ.get('GH_TOKEN')
auth = (username, token)


def check_version(current_version):
    resp = requests.get(URL, auth=auth)
    data = resp.json()
    new_version = data['tag_name']
    print("Current version: " + current_version)
    print("Latest version: " + new_version)
    data = []
    if new_version == current_version:
        return (None, None)
    else:
        for arch in ARCH:
            for asset in data['assets']:
                if asset['name'] == f'ping_exporter_{new_version}_linux_{arch}.deb':
                    print(f'ping_exporter_{new_version}_linux_{arch}.deb')
                    data.append(
                        (asset['browser_download_url'], asset['name'], arch))

        if len(data) == 0:
            print("Error! New version but no matching assets found")
            return (None, None)

        else:
            return (new_version, data)


def build_package(version, location, data):

    link = data[0]
    # print(link)
#    print(f'Location {location}')
    for arch in data:
        bashCommand = f"sh ./recipes/prometheus-ping-exporter/build_{arch[2]}.sh "+link + " " + \
            version + " "+location + \
            f'prometheus-ping-exporter_{version}_linux_amd64.deb' + \
            " >/tmp/deblog"
        os.system(bashCommand)
        print("Ran Bash Script")
