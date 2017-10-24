Mobile Control

With this app, you can move your mouse using the phone accelerometer, click it using your voice and set the screen brightness to match your phone light sensor.

You will need the following packages:

BeautifulSoup4 (pip install beautifulsoup4)

wmi (pip install wmi)

pynput (pip install pynput)

You'll also need and app that turns your android phone into a transmitter. I used Sensor Node:

https://play.google.com/store/apps/details?id=com.mscino.sensornode&hl=en

Instructions:
1. Open the app, in settings change the refresh rate to 70ms.
2. Select xml stream
3. Check the accelerometer, light intensity and noise level boxes
4. Turn off your firewall, or enable the app to connect to the computer.
5. Insert your IP adress and your desired port (note that if you change the port in the app, you also need to change it in the script.)
6. Press stream.
7. Tilt your phone to move the mouse and raise your voice to click. The brightness changes according to the light intensity.
8. Enjoy!

App written by Haim Leshem.
Feel free to make any changes and improvements to the script!
