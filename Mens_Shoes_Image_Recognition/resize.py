import sys
from PIL import Image
from os import listdir

y=sys.argv[1]
files=[x for x in listdir(y) if x[-4:]=='.jpg']
for x in files:
    ## print 'Processing image :',x
    dloc=''.join([y,x])
    im=Image.open(dloc)
    w,h=im.size
    ## Images are cropped into a square
    crop_im=im.crop((0,(h-w)/2,w,h-((h-w)/2)))
    resize = crop_im.resize((200, 200))
    resize.save(dloc)
