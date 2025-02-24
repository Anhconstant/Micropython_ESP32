import network
def wifi_do_connect(wf_ssid,wf_pass):
    wlan = network.WLAN(network.WLAN.IF_STA)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(wf_ssid, wf_ssid)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ipconfig('addr4'))
def wifi_create_AP( wf_name, wf_pass):
    ap = network.WLAN(network.WLAN.IF_AP)
    ap.active(True)
    ap.config(ssid='ESP32WF',key='12345678')
    ap.config(max_clients=10)
    print('SSID:',ap.config('essid'))
    print('PASS:',ap.config('password'))
    print('ip:'ap.ipconfig('addr4')[](0))