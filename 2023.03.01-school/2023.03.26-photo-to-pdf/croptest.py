from PIL import Image
import cv2
import glob
import re
# ('./*.gif

img = Image.open('./imgs/2.jpg')

# cv2.imshow('test', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

width, height = img.size
img = img.crop((110, 60, width - 110, height - 60))


img.show()

# img1.show()



# image_list = []
# filename_list = []
# for filename in glob.glob('./imgs/*.jpg'):
#     filename_list.append(filename)

# p = re.compile(r'\d+')
# filename_list.sort(key=lambda s: int(p.search(s).group()))

# for filename in filename_list:
#     im = Image.open(filename)
#     im = im.convert('RGB')
#     image_list.append(im)

# image_list[0].save(r'lesson1.pdf', save_all=True, append_images=image_list[1:])