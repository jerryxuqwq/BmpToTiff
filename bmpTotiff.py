from PIL import Image
from PIL import TiffImagePlugin
import os
from os import path
import glob
from io import BytesIO
file_names = path.dirname('.')
for file_names in glob.glob('*.bmp'):
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
