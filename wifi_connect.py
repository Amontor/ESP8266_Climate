'''
连接路由器模块
'''

import time
import network
from led import *

ssid = "Tenda-109"
password = "15937644329"

def wifi_connect():
    wlan = network.WLAN(network.STA_IF)     #使用STA模式
    wlan.active(True)   #激活网络
    start_time = time.time()    #记录时间，用于超时判断

    if not wlan.isconnected():
        print("connecting to network...")
        wlan.connect(ssid, password)

        while not wlan.isconnected():
            led.on
            time.sleep_ms(300)
            led.off
            time.sleep_ms(300)

            if time.time() - start_time > 15:   #连接超时
                print("WIFI connect TimeOut!")
                break;
    else:
        led.off
        print("network information:", wlan.ifconfig())