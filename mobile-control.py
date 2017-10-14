from pynput.mouse import Button, Controller
import wmi
import socket
import bs4
import time

host = socket.gethostbyname(socket.gethostname())
port = 50000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind((host, port))
# for debugging
# print("success")
mouse = Controller()


def sensor_data():
    src = bs4.BeautifulSoup(data, 'lxml')
    x = src.find('accelerometer1')
    X = int(float(x.text))
    y = src.find('accelerometer2')
    Y = int(float(y.text))
    single_click = src.find('noiselevel')
    brightness = src.find('lightintensity')
    mouse.move(-X * 4, -Y * 4)

    # left click
    if int(float(single_click.text)) >= 60:
        mouse.click(Button.left)

    # brightness modifier
    if 0 <= int(float(brightness.text)) <= 100:
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(int(float(brightness.text)), 0)

    if int(float(brightness.text)) > 100:
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(100, 0)


while True:
    data, addr = sock.recvfrom(4800)
    # for debugging
    # print(data)
    sensor_data()
    time.sleep(0)
