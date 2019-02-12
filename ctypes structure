import ctypes
from ctypes import *
import re
import numpy
import time
import struct

class Msg_DetectReq(Structure):
    _fields_=[('eventPath', c_char_p) ]
    
class Msg_Detect_Result(Structure):
    _fields_=[ ('eventNum', c_uint),
               ('allNum', c_uint),
                ('costTime', c_float)           
    ]
    
class Event_Info(Structure):
    _fields_=[ ('eventName', c_char*256),
                ('start_time', c_char*64),
                ('end_time', c_char*64),
                ('detect_chance', c_float)
    ]
    
if __name__=="__main__":    
    line = ['YA22.116', 
            '2013-04-26T00:00:00.000000Z', 
            '2013-04-26T00:00:10.000000Z', 
            '0.99807584', 
            '[UTCDateTime(2013, 4, 26, 0, 0)]', 
            '[UTCDateTime(2013, 4, 26, 0, 0, 9, 995000)]']
    name = line[0].split(',')[0]
    print(name)
    
    event_info = Event_Info()
    event_info.eventName = name.encode("utf-8")
    event_info.detect_chance = float(line[3])
    event_info.start_time = line[4].encode("utf-8")
    event_info.end_time = line[5].encode("utf-8")
    
    print(event_info.eventName)
    print(event_info.detect_chance)
    print(event_info.start_time)
    print(event_info.end_time)
    print(pointer(event_info))
    
    print(string_at(ctypes.pointer(event_info), ctypes.sizeof(event_info)))
'''   
    res = re.finditer(r"\d+",line[4])
    tm = (numpy.uint64)(0)
    index = 0
    for match in res:
        print(match.group())
        if index == 0: 
            tm = (tm + (numpy.uint64)(match.group()))*12
        elif index == 1:
            tm = (tm + (numpy.uint64)(match.group()))*12
        elif index == 2:
            tm = (tm + (numpy.uint64)(match.group()))*24
        elif index == 3:
            tm = (tm + (numpy.uint64)(match.group()))*60
        elif index == 4:
            tm = (tm + (numpy.uint64)(match.group()))*60
        elif index == 5:
            tm = (tm + (numpy.uint64)(match.group()))*1000
        elif index == 6:
            tm = (tm + (numpy.uint64)(match.group()))
         

        index = index + 1

    timeArray = time.strptime("2018") 
    timestamp = time.mktime(timeArray) 
    time_now = time.time()         
    print(tm-28800000000)
''' 
