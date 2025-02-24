from machine import Pin
import time
import network
import usocket as socket

time.sleep(2)

print("Webserver Start")

led = Pin(15, Pin.OUT)  # Warning
client.init()  # init device - device wireless

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 80
s.bind((host, port))
s.listen(5)

while True:
    html = '''<!DOCTYPE html>
    <html>
    <center><h2> Fire Warning Websever </h2></center>
    <form>
    <center>
    '''
    floor1 = '\n <h3> Floor1 </h3>'
    floor1 = floor1 + '\n <p>gas = ' + str(sensor.read_gas(f1)) + '%  |  Temp = ' + str(
        sensor.read_temp(f1)) + '&deg;C  | FireDetect :' + str(sensor.fire_detect(f1)) + '</p>'
    floor2 = '\n <h3> Floor2 </h3>'
    floor2 = floor2 + '\n <p>gas = ' + str(sensor.read_gas(f2)) + '%  |  Temp = ' + str(
        sensor.read_temp(f2)) + '&deg;C  | FireDetect :' + str(sensor.fire_detect(f2)) + '</p>'
    floor3 = '\n <h3> Floor3 </h3>'
    floor3 = floor3 + '\n <p>gas = ' + str(sensor.read_gas(f3)) + '%  |  Temp = ' + str(
        sensor.read_temp(f3)) + '&deg;C  | FireDetect :' + str(sensor.fire_detect(f3)) + '</p>'
    warning = '''
    <button name="Warning" value='ON' type='submit'>ON</button>
    <button name="Warning" value='OFF' type='submit'>OFF</button>
    </center>
    '''
    html += floor1 + floor2 + floor3 + warning

    connection_socket, address = s.accept()
    print('got a connection', address)
    request = connection_socket.recv(1024)
    print('content', request)
    request = str(request)
    LED_ON = request.find('/?Warning=ON')
    LED_OFF = request.find('/?Warning=OFF')
    print(LED_ON, LED_OFF)
    if (LED_ON == 6):
        led.value(1)
    if (LED_OFF == 6):
        led.value(0)
    response = html
    connection_socket.send(response)
    connection_socket.close()
