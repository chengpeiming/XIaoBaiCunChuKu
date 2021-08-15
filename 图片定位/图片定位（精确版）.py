import re

import exifread

f = open("4.jpg", 'rb')  # "4.jpg"为图片路径

tags = exifread.process_file(f)

long = str(tags.get('GPS GPSLongitude', '0')).split("[")[1].split("]")[0].split(",")
print("经度：", float(long[0]) + float(long[1]) / 60 + float(long[2].split("/")[0]) / float(long[2].split("/")[1]) / 3600)

lat = str(tags.get('GPS GPSLatitude', '0')).split("[")[1].split("]")[0].split(",")
print("纬度：", float(lat[0]) + float(lat[1]) / 60 + float(lat[2].split("/")[0]) / float(lat[2].split("/")[1]) / 3600)

for key in tags:
    if key == "GPS GPSLongitude":
        print("高度基准: ", tags['GPS GPSAltitudeRef'])
        print("海拔高度: ", tags['GPS GPSAltitude'])
    if re.match('Image Make', key):
        print('品牌信息: ', tags[key])
    if re.match('Image Model', key):
        print('具体型号: ', tags[key])
    if re.match('Image DateTime', key):
        print('拍摄时间: ', tags[key])
    if re.match('Image ImageDescription', key):
        print('图像描述: ', tags[key])
    if re.match('EXIF ExifImageWidth', key):
        print('照片尺寸: ', tags[key], '*', tags['EXIF ExifImageLength'])
