#导入词云的包 
from wordcloud import WordCloud 
#导入matplotlib作图的包 
import matplotlib.pyplot as plt 
# #读取文件,返回一个字符串，使用utf-8编码方式读取，该文档位于此python同以及目录下
# f = open('NINETEEN+EIGHTY-FOUR.txt','r',encoding='utf-8').read()
# #生成一个词云对象
# wordcloud = WordCloud( background_color="white", #设置背景为白色，默认为黑色
#         width=1500, #设置图片的宽度
#         height=960, #设置图片的高度
#         margin=10 #设置图片的边缘
#         ).generate(f)
# # 绘制图片
# plt.imshow(wordcloud)
# # 消除坐标轴
# plt.axis("off")
# # 展示图片
# plt.show()
# # 保存图片
# wordcloud.to_file('my_test2.png')






import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
text = ''
with open('NINETEEN+EIGHTY-FOUR.txt', 'r', encoding='utf8') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
# sep’.join（seq）以sep作为分隔符，将seq所有的元素合并成一个新的字符串
text += ' '.join(jieba.cut(line))
backgroud_Image = plt.imread('man.jpg')
print('加载图片成功！')
'''设置词云样式'''
wc = WordCloud(
    background_color='white',# 设置背景颜色
    mask=backgroud_Image,# 设置背景图片
    font_path='C:\Windows\Fonts\msyhbd.ttc',  # 若是有中文的话，这句代码必须添加，不然会出现方框，不出现汉字
    max_words=2000, # 设置最大现实的字数
    stopwords=STOPWORDS,# 设置停用词
    max_font_size=150,# 设置字体最大值
    random_state=30# 设置有多少种随机生成状态，即有多少种配色方案
)
wc.generate_from_text(text)
print('开始加载文本')
#改变字体颜色
img_colors = ImageColorGenerator(backgroud_Image)
#字体颜色为背景图片的颜色
wc.recolor(color_func=img_colors)
# 显示词云图
plt.imshow(wc)
# 是否显示x轴、y轴下标
plt.axis('off')
plt.show()
# 获得模块所在的路径的
d = path.dirname(__file__)
# os.path.join()：  将多个路径组合后返回
wc.to_file(path.join(d, "h11.jpg"))
print('生成词云成功!')
