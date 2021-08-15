import itertools
import zipfile

# 构造所有密码元素如果有其他特殊字符也可以自己添加
lis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z', ',', '.', '!', '@', '#', '$', '%',
       '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{',
       ']', '}', '\ ', '|', ';', ':', '"', "'", ',', '<', '.',
       '>', '/', '?', '`', '~', ]

temp = True  # 用于破解成功后，停止循环的变量

for x in range(1, 17):  # 设置密码的位数 1~17 位
    if temp:
        def keyword():
            key1 = itertools.product(lis, repeat=x)
            key2 = (''.join(i) for i in key1)
            return key2


        def trypassword(password):
            try:
                ZIPFILE = zipfile.ZipFile(r'E:\Pyhton开发工作区\python小程序\压缩包破解\待破解\1.zip')  # 要破解的文件地址
                ZIPFILE.extractall(path=r'E:\Pyhton开发工作区\python小程序\压缩包破解\破解完成', pwd=password.encode('utf-8'))  # 解压到哪个路径
                print(f"解压成功,正确密码为：{password}")
                global temp
                temp = False
                return True
            except:
                print(f"解压失败,尝试密码为：{password}")
                return False


        for p in keyword():
            if trypassword(p):
                break
