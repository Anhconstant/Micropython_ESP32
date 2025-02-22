from machine import Pin
import time
import os
import urequests
import secret

GITHUB_URL = secret.secret_url
wf_id = secret.wifi_ssid
wf_pass = secret.wifi_pass
current_ver = str(secret.current_ver)
url_ver = secret.url_ver

print("in boot")


def do_connect():
    import network
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print("connecting to network..")
        wlan.connect(wf_id, wf_pass)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ipconfig('addr4'))


def check_ver(url, current_ver):
    res_ver = urequests.get(url)
    return int(res_ver.text)


def download_file(url, filename):
    print(f"Downloading {filename} from {url}...")
    response = urequests.get(url)

    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"Download {filename} completed!")
    else:
        print(f"Fail download file, code: {response.status_code}")

    response.close()


do_connect()

git_ver = check_ver(url_ver, current_ver)

if str(git_ver) != str(current_ver):
    print('starting delete app_current.py')
    time.sleep(2)
    os.remove("app_current.py")
    print('update file app_current.py')
    download_file(GITHUB_URL, "app_current.py")

    file_path = "secret.py"
    with open(file_path, "r") as file:
        lines = file.readlines()
    data_write = ""
    for i in range(len(lines)):
        if "current_ver" in lines[i]:
            lines[i] = "current_ver=" + str(git_ver)
        data_write += lines[i]
    with open(file_path, "r+") as file:
        file.write(data_write)
print('run app')
import app_current



