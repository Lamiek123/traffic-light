import network
import socket
from time import sleep
from battlebot2 import *
import machine

page = open("index.html", "r")
html = page.read()
#print(html);
page.close()

ssid='CYBERTRON'
password='Mr.LamYo'



def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    #Start a web server
    #servo1 = slow_servo.Slow_Servo(1)	#create servo object on pin 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print (request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request.startswith('/slider'):
            slider_val = int(request.split('?')[1])
            print ('slider: ', slider_val)
            if slider_val >= 0:
                move_left_forward()
                setASpeed(slider_val)
            else:
                move_left_backward()
                setASpeed(-slider_val)
            
            
        elif request.startswith('/Bslider'):
            Bslider_val = int(request.split('?')[1])
            print ('Bslider: ', Bslider_val)
            if Bslider_val >= 0:
                move_right_forward()
                setBSpeed(Bslider_val)
            else:
                move_right_backward()
                setBSpeed(-Bslider_val)

            
            
            
#             servo1.set_angle(slider_val,1000)
       # html = page()
        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html)
        client.close()


try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
