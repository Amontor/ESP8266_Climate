'''
DS18B20 模块，用于驱动传感器获取外部温度
'''

from machine import Pin
import time
import onewire
import ds18x20

# 定义外设控制对象,传感器连接到DPIO13上(D7)
ds18b20 = ds18x20.DS18X20(onewire.OneWire(Pin(13)))

#扫描ds18b20设备
roms = ds18b20.scan()  # 扫描总线上的设备
print('扫描发现的设备: ', roms)

def read_ds18b20():  # 创建一个读取温度的函数
    ds18b20.convert_temp()  # 温度转换
    for rom in roms:  # 循环打印出设备列表
        temp = ds18b20.read_temp(rom)  # 读出该设备的温度
        if isinstance(temp, float):  # 以小数点后2位输出，例如23.35
            temp = round(temp, 2)
            return temp
    return 0