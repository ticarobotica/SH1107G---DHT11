from machine import Pin, SoftI2C
from time import sleep_ms
from sh1107g import SH1107G
from dht import DHT11


i2c_oled=SoftI2C(sda=Pin(8), scl=Pin(9), freq=100000)
oled=SH1107G(i2c_oled)

pin_dht=Pin(20, Pin.IN)
senzor_dht=DHT11(pin_dht)

while 1:
    senzor_dht.measure()
    temp=senzor_dht.temperature()
    humi=senzor_dht.humidity()
    print("Temperatura este ", temp," ", "Umiditatea este =", humi," ", end="\r")
    oled.text("Temp = "+str(temp),1,1)
    oled.text("Humi = "+str(humi),1,10)
    oled.update_all()
    sleep_ms(1000)
    oled.fill(0)
        
