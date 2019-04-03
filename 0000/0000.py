from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# 导入png图片
img = Image.open("Test.png")

# 设置在图片上把(0,0)和(360,360)的大小截取出来
# 毕竟头像应该是方的
box = (0, 0, 360, 360)
img = img.crop(box)
# 换成缩略图
img.thumbnail((128, 128))

# 设置字体
font = ImageFont.truetype("arial.ttf", size=35)

# 在图片上创建画笔
draw = ImageDraw.Draw(img)

# 在图片上画一个圆
# 其中，[(x0, y0), (x1, y1)] (x0, y0)是椭圆的一个顶点，(x1, y1)是另一个顶点
# fill是填充颜色
draw.ellipse([(90, 0), (120, 30)], fill=(255, 0, 0))
# 在图上写字，字体设为font
draw.text((96, -4), "4", (255, 255, 255), font=font)

img.save("Target.png")
# print("success")
