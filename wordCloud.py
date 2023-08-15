from wordcloud import WordCloud
import matplotlib.pyplot as plt
from imageio import imread
import numpy as np
from PIL import Image

select = 0 # 选择使用文本还是此处输入
if select:
  file = open('word_cloud.txt', encoding="utf-8")
  text = file.read()#文本
else:
  text = "茯 茯基共 用仍遥昣  别 吸 昣蝇明 丽地" \
        "华莱士 百暧城 肝 仍埏 我就 是刘 "

my_mask = np.array(Image.open('xinxing2.png'))#图片

wcd = WordCloud(background_color='white',min_font_size=24 ,\
          font_path="C:\Windows\Fonts\msyh.ttc", \
            width=1920, height=1080, max_words=180, max_font_size=90, repeat=True
                 )

# 控制是否使用自定图片形状
# wcd.mask = my_mask

wcd.generate(text)
plt.imshow(wcd, interpolation="bilinear")
plt.axis("off")
plt.show()

