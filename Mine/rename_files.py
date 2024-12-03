import os

dir = '/Users/hang/Downloads/无敌绿宝书音频 N5/'
x = os.listdir(dir)
for file in x:
    file_name = os.path.basename(file)
    # 替换文件名中的字符串
    new_file_name = file_name.replace('石', '书')
    os.rename(dir + file_name, dir + new_file_name)
