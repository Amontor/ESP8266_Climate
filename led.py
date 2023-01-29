'''
LED设备,可以用于指示开发板运行状态
'''

from machine import Pin

led = Pin(2, Pin.OUT)