import utime
from machine import UART

def read_sentence(uart):
    gpsData = uart.read().decode()
    for sentence in gpsData.splitlines():
        if "GPGGA" in sentence:
            return sentence


def parse_position(sentence):
    fields = sentence.split(',')
    print(fields)
    if fields[6]=="1":
        gpsTime = fields[1][:2]+":"+fields[1][2:4]+":"+fields[1][4:6]
        latitude = float(fields[2][:2]) + float(fields[2][2:]) / 60
        longitude = float(fields[4][:3]) + float(fields[4][3:]) / 60

        if fields[3] == 'S':
            latitude = -latitude
        if fields[5] == 'W':
            longitude = -longitude
        print(gpsTime, latitude, longitude)
        return gpsTime, str(latitude), str(longitude)
    else:
        return "no gps data, please retry"