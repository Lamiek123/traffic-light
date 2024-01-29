import network
import socket
from time import sleep
from battlebot3 import *
from Slow_Servo import *
import machine

page = open("index1.html", "r")
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
                
                
        elif request.find('servoslider') > -1:
            servoslider_val = request.split('?')[1]
            print (servoslider_val)
            servo1 .set_angle(servoslider_val,1000)

        client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html)
        client.close()


try:
    ip = connect()
  
    serve(open_socket(ip))
except KeyboardInterrupt:
    machine.reset()
