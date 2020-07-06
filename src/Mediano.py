from PIL import Image

im = Image.open('image2.jpg')
members = [(0,0)] * 9
width = im.size[0]
height = im.size[1]
#newimg = Image.new("RGB",(width,height),"white")
for i in range(1,width-1):
    for j in range(1,height-1):
        members[0] = im.getpixel((i-1,j-1))
        members[1] = im.getpixel((i-1,j))
        members[2] = im.getpixel((i-1,j+1))
        members[3] = im.getpixel((i,j-1))
        members[4] = im.getpixel((i,j))
        members[5] = im.getpixel((i,j+1))
        members[6] = im.getpixel((i+1,j-1))
        members[7] = im.getpixel((i+1,j))
        members[8] = im.getpixel((i+1,j+1))
        members.sort()
        im.putpixel((i,j),(members[4]))
im.show()