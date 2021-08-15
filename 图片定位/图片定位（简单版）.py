import exifread
import re


def read():
    GPS = {}
    date = ''
    f = open("4.jpg", 'rb')
    contents = exifread.process_file(f)
    for key in contents:
        if key == "GPS GPSLongitude":
            print("纬度 =", contents[key], contents['GPS GPSLongitudeRef'])
        elif key == "GPS GPSLatitude":
            print("经度 =", contents[key], contents['GPS GPSLatitudeRef'])

read()