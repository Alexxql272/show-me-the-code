from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random

background_color = (0, 0, 0)

# 依顺序把img的每个像素的RGB改变随机值，第二个参数是是否把背景模糊化，默认要模糊
def change_to_mosaic(img, change_background=True):
    i = 0
    # 遍历每个像素
    for i in range(400):
        j = 0
        for j in range(200):
            pixel = list(img.getpixel((i, j)))
            # 如果是背景颜色，就不改变
            # 目前好像还没有找到让它和background_color直接相等的办法
            if change_background == False and (pixel == [0, 0, 0] or pixel == [255, 255, 255]):
                continue
            k = 0
            # 对RGB的三个值随机改变
            for k in range(3):
                change_color = random.randint(-100,100)
                pixel[k] += change_color
            img.putpixel((i,j), tuple(pixel))
    return img

# 创建新的图片
img1 = Image.new(mode='RGB', size=(400,200), color=background_color)
# 创建画笔
draw_pen = ImageDraw.Draw(img1, mode='RGB')
font1 = ImageFont.truetype("arial.ttf", size=110)

count = 0
# 生成6个验证码
while count < 6:
    i = random.randint(1, 3)
    # 如果随机到1就生成数字
    if i == 1:
        int_char = random.randint(48, 57)
    # 如果2就生成大写字母
    elif i == 2:
        int_char = random.randint(65, 90)
    # 3 生成小写字母
    elif i == 3:
        int_char = random.randint(97, 122)

    # 随机改变字母的y轴位置
    random_ypos = random.randint(-30, 30)
    # 随机改变字母的x轴位置
    random_xpos = random.randint(-15, 15)
    # 生成随机的颜色
    random_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
    # 转换成字符
    generate_char = chr(int_char)
    # 写字
    draw_pen.text([20+count*(60)+random_xpos,30+random_ypos], generate_char, random_color, font=font1)
    count += 1

# 把生成好的图片随机马赛克化
img1 = change_to_mosaic(img1)
# 转换成缩略图，不消除锯齿
img1 = img1.resize((100,50))
with open('pic.png','wb') as f:
    # 保存
    img1.save(f, format='png')

img1.show()
