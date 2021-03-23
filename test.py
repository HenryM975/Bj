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
    #for element1 in part_of_fullist:
        #element1 = element1.replase(' ', '')
    fullist.append(part_of_fullist)
print(fullist)
print(fullist[1])