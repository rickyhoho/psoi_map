from PIL import Image
import os

#10122020200031_200
#just for copy, ignore it
file = "./" + input("input file name:")
filemap = file + "/map"
filecode = file + "/code"
file_new = file + "/new"

if not os.path.exists(filemap) or not os.path.exists(filecode):
    print("ERROR")
    input()
    exit(0)

if not os.path.exists(file_new):
    os.mkdir(file_new)
else:
    print("file created")

def get_concat_h(im1, im2):
    if im1.height < im2.height:
        im1 = im1.resize((min(int(im1.width * 1.5), int(im1.width * im2.height / im1.height)), min(int(im1.height * 1.5), im2.height)))
    else:
        im2 = im2.resize((min(int(im2.width * 1.5), int(im2.width * im1.height / im2.height)), min(int(im2.height* 1.5), im1.height)))

    dst = Image.new('RGB', (im1.width + im2.width, max(im1.height,im2.height)), "WHITE")
    if im1.height > im2.height:
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, int((im1.height - im2.height) / 2)))
    else:
        dst.paste(im1, (0, int((im2.height - im1.height) / 2)))
        dst.paste(im2, (im1.width, 0))
        
    '''dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))'''
    return dst
    
for i in range(1, int(input("number of photo:")) + 1):
    im1 = Image.open(filemap + "/" + "%05d" % i + ".png")
    im2 = Image.open(filecode + "/" + "%05d" % i + ".png")
    get_concat_h(im2, im1).save(file_new + "/" + "%05d" % i + ".png")
    print(i)
input("finish")