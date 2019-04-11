import os

# 取得文件后缀
def get_suffix_name(string):
    type_name = ''
    i = 0
    while i < len(string):
        if string[i] == '.':
            break
        i += 1
    while i < len(string) - 1:
        i += 1
        type_name += string[i]
    return type_name

# 基础路径，我的vs2017的repos的路径
base_path = 'C:/Users/27246/source/repos'
folder_list = os.listdir(base_path)
# print(folder_list)

ans = 0

# 遍历repos下的所有子文件夹
for folder in folder_list:
    # vs存cpp和h的文件夹名字和父文件夹名字一样
    child_folder_path = base_path + '/' + folder + '/' + folder
    child_folder_list = os.listdir(child_folder_path)
    # print(child_folder_list)
    # 遍历子文件夹的所有文件
    for file_name in child_folder_list:
        suffix_name = get_suffix_name(file_name)
        # 找出所有后缀为cpp或者h，不统计pch.h
        if (suffix_name == 'h' or suffix_name == 'cpp') and file_name != 'pch.h':
            file_path = child_folder_path + '/' + file_name
            hFile = open(file_path, encoding='utf-8', errors='ignore')
            # text = hFile.read().split()
            # print(text)
            # 这里有一点很重要，如果read了hFile的话，再遍历就会是字符遍历，不read的话就是一行一行的遍历
            # 我们要统计行数，所以不应该read
            for line in hFile:
                ans += 1
                # print(line)
print(ans)
