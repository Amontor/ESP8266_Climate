import led
import ds18b20
from wifi_connect import *
from RTC_net import *
from machine import SoftI2C
from ssd1306 import SSD1306_I2C

def main():
    week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    led.on
    
    # 联网
    time.sleep(0.5)
    wifi_connect()
    time.sleep(0.5)
    #通过网络校准时间
    sync_ntp()
    time.sleep(0.5)

    # 设置OLED屏,
    # ESP8266没有硬件I2C，使用软件I2C, SDA、SCL分别为GPIO4(D2),GPIO5(D1)
    i2c= SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)
    oled = SSD1306_I2C(128, 64, i2c)
    oled.fill(0)    #清屏
    oled.show()     #执行显示
    oled.text("Hello MicroPython", 0, 0, 1) #显示字符串
    oled.text("Welcome to ESP-12", 0, 16, 1)
    oled.show()
    time.sleep(2)
    oled.fill(0)
    oled.show()

    rtc = RTC()
    status = 1
    while True:
        oled.fill(0)
        oled.show()

        date_time = rtc.datetime()
        temp = ds18b20.read_ds18b20()

        oled.text("%d-%d-%d" %(date_time[0], date_time[1], date_time[2]), 3, 0, 1)
        oled.text("%s" %(week[date_time[3]]), 4, 16, 1)
        oled.text("%02d:%02d:%02d" %(date_time[4], date_time[5], date_time[6]), 4, 32, 1)
        oled.text("%.2f C" %(temp), 4, 48, 1)
        oled.show()

    
if __name__ == '__main__':
    main()