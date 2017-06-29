import re
page_nums = 30
new_src = []
image_src=['http://i.meizitu.net/2016/06/15b01.jpg']
image_new_src = "".join(image_src)
pattern = re.compile('http://i.meizitu.net/(\w+)/(\w+)/(\w+)(\d){2}.jpg')
result = re.match(pattern,image_new_src)
ma = result.groups()
print(ma)
print(result.groups(-1))
for i in range(int(result.groups()[-1]),page_nums + 1):
    if i < 10:
        src_link = 'http://i.meizitu.net/{}/{}/{}0{}'.format(ma[0],ma[1],ma[2],i)
        new_src.append(src_link)
    elif i > 9:
        src_link = 'http://i.meizitu.net/{}/{}/{}{}'.format(ma[0], ma[1], ma[2], i)
        new_src.append(src_link)
    else:




        print(new_src)
        print("Check src")




