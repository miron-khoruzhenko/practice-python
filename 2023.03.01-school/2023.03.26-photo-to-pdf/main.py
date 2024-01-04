from PIL import Image
import glob
import re
# ('./*.gif

image_list = []
filename_list = []
for filename in glob.glob('./imgs/*.jpg'):
    filename_list.append(filename)

p = re.compile(r'\d+')
filename_list.sort(key=lambda s: int(p.search(s).group()))

for filename in filename_list:
    im = Image.open(filename)

    width, height = im.size
    im = im.crop((110, 60, width - 110, height - 60))
    im = im.convert('RGB')
    image_list.append(im)

image_list[0].save(r'lesson1.pdf', save_all=True, append_images=image_list[1:])