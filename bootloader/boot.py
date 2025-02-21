# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
# import webrepl
# webrepl.start()
from machine import Pin
import time
import os
import urequests
import secret  #include string follow:

GITHUB_URL = secret.secret_url
wf_id = secret.wifi_ssid
wf_pass = secret.wifi_pass

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


def download_file(url, filename):
    print(f"Downloading {filename} from {url}...")
    response = urequests.get(url)

    if response.status_code == 200:
        with open(filename, "w") as f:
            f.write(response.text)
        print(f"Download {filename} completed!")
    else:
        print(f"Fail, code: {response.status_code}")

    response.close()


do_connect()

print('do you want update? y/n')
n = input()

if n == 'y':
    print('starting delete main.py')
    time.sleep(2)
    os.remove("main.py")
    print('update file main.py')
    download_file(GITHUB_URL, "main.py")
print('run main')
import main