import re
# path = input("Enter file name:")
# if len(path) < 1:
path = "test.txt"
xFile = open(path)
newDict = dict()
# 遍历文件的所有行
for line in xFile:
    # 跳过空行
    if len(line) < 1:
        continue
    # 用正则表达式找出所有的单词
    # 如果直接用split的话会连带标点
    pieces = re.findall('[a-zA-Z]+', line)
    for word in pieces:
        # 全部变成小写，以统计所有的单词（不区分大小写）
        word = word.lower()
        newDict[word] = newDict.get(word, 1) + 1
maxKey = None
maxVal = None
for key, val in newDict.items():
    if maxVal == None:
        maxVal = val
        maxKey = key
    elif val > maxVal:
        maxVal = val
        maxKey = key
print(maxKey, maxVal)