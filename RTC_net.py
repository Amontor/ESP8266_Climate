'''
RTC 模块,从网络校准时间
'''

from machine import RTC
import ntptime
from machine import Timer

# 通过网络校准时间
def sync_ntp():
    ntptime.NTP_DELTA = 3155644800  # 可选 UTC+8偏移时间（秒），不设置就是UTC0
    # ntptime.host = 'ntp1.aliyun.com'  # 可选，ntp服务器，默认是"pool.ntp.org" 这里使用阿里服务器
    ntptime.settime()  # 修改设备时间
