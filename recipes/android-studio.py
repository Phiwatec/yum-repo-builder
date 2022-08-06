import requests
from bs4 import BeautifulSoup
import subprocess

URL = "https://developer.android.com/studio#downloads"
DL_URL="https://redirector.gvt1.com/edgedl/android/studio/install/{version}/{file}"








def check_version(current_version):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.select('button[data-modal-dialog-id="studio_chrome_os_bundle_download"]')
    for item in results:
        for content in item.contents:
                file=content
                break
        break

    version=file.split('-')[2]
    if version == current_version:
        return False
    else:
        return (version,file)


def build_package(version,location):
    link=DL_URL.format(version=version[0],file=version[1])
    print(link)
    bashCommand = "sh ./recipes/android-studio/build.sh "+link  + " " + version[0] + " "+location+" >/tmp/deblog"
    print(bashCommand)
    process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE,shell=True)

    print("Ran Bash Script")