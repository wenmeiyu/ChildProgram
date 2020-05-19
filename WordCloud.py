from wordcloud import WordCloud
import numpy
import PIL.Image as Image
import xlrd

with xlrd.open_workbook("./data/majors.xlsx", encoding_override="utf-8")as excel:
    sheet = excel.sheets()[0]  # 读取第一个表
    rows = sheet.row_values(0)  # 读取第一行
    print(rows)  # 打印第一行
    clou_list = sheet.col_values(4)  # 读取第五列
    clou_list = clou_list[1:]
    print(clou_list)  # 打印第五列
    # 把列表拼接为空格分割的文本
    text = ""
    for clou in clou_list:
        print(clou)
        text = text+" "+clou
    print(text)
    # 图片遮罩层
    mask_pic = numpy.array(Image.open("./data/china.png"))
    # 将参数mask设值为：mask_pic 造型遮盖
    wordcloud = WordCloud(font_path="./data/simhei.ttf", mask=mask_pic).generate(text)
    image = wordcloud.to_image()
    image.show()

