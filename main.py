# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
#PARS
txt_namesfile = open('C:\\Users\\user\\Desktop\\names.txt', encoding='UTF-8')
linelist = []
for line in txt_namesfile:
    linelist.append(line)
print(linelist)
fullist = []
for element in linelist:
    part_of_fullist = []
    element = element.replace('\n', '')
    a, b = element.split(',')
    part_of_fullist.append(a)
    part_of_fullist.append(b)
    part_of_fullist[1] = part_of_fullist[1].replace(' ', '')
    fullist.append(part_of_fullist)
print(fullist)
#/PARS
photo_name = 1
while True:
    txt_file_element = int(photo_name - 1)
    line_data = (fullist[txt_file_element])



    #name = input("Имя Фамилия: ")
    name_line = fullist[txt_file_element]
    name = name_line[0]

    template_line = fullist[txt_file_element]
    template = template_line[1]
    #template = 'nmg'

    #photo_name = input("Файл с фото: ")


    #Решение проблем с кирилицей
    font = ImageFont.truetype('C:\\Users\\user\\Desktop\\Oswald-Medium.ttf', 40, encoding='UTF-8')#in Fonts path
    #PARS

    #name = u'грнаесаче'
    #name.encode('latin-1', 'replace')
    #name.encode('utf-8')
    im = Image.open('C:\\Users\\user\\Desktop\\' + template + '.jpg').convert("RGBA")#change path
    try:
        photo = Image.open('C:\\Users\\user\\Desktop\\' + str(photo_name) + '.jpeg').convert("RGBA")#change path
    except:
        try:
            photo = Image.open('C:\\Users\\user\\Desktop\\' + str(photo_name) + '.png').convert("RGBA")#change path
        except:
            photo = Image.open('C:\\Users\\user\\Desktop\\' + str(photo_name) + '.jpg').convert("RGBA")#change path


    print(im.size)
    print(photo.size)
    first_im_w, first_im_h = im.size
    first_photo_w, first_photo_h = photo.size
    photo_coefficient = 250/first_photo_w
    second_photo_h = first_photo_h * photo_coefficient
    if int(second_photo_h) > 420:
        second_photo_h = 420

    watermark = photo.resize((250, int(second_photo_h)), Image.ANTIALIAS) #photo=>watermark #размер
    draw_text = ImageDraw.Draw(im)
    #text_w, text_h = draw_text.textsize(name)
    w, h = draw_text.textsize(name, font=font)
    draw_text.text(
        ((677-w)/2,740),
        name,
        font=font,
        fill=('#000000')
    )
    im_h = int(((730 - 310 - int(second_photo_h))/2) + 310)
    print(im_h)
    im.paste(watermark, (210, im_h), watermark)
    #im.show()
    #print(im.size)
    print(watermark.size)
    #SAVE
    filename_start_list = name.split(' ')
    filename = filename_start_list[0]
    im.save('C:\\Users\\user\\Desktop\\pillow\\' + filename + str(photo_name) + '.png', 'png')#change res path
    #/SAVE
    print(photo_name)
    photo_name+=1

#калибровка по вертикали аналогично фио