from PIL import Image
from PIL import TiffImagePlugin
import os
from os import path
import glob
from io import BytesIO
file_names = path.dirname('.')
for file_names in glob.glob('*.bmp'):#找出所有的后缀为bmp的格式的图片
	file_path = r'./'+file_names
	out_path =os.path.splitext(file_path)[0]+'.tiff'
	print(file_names)
	im=Image.open(file_path)
	#im.save(out_path)
	png1 = BytesIO()
	im.save(png1, format='png')
	png2 = Image.open(png1)
	png2.save(out_path)
	png1.close()
print("done")
	
#with Image(file_name) as img:
#    img.resize(200, 200) # width, height
#    img.save(filename = 'result1.jpg') # png, jpg, bmp, gif, tiff All OK