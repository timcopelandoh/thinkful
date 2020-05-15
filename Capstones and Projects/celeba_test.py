from PIL import Image

path = '../../../Downloads/img_align_celeba/'

image = Image.open(path + '000001.jpg')

#image.crop(box = [60,70,120,170]).show()




file_list = [str(i) for i in range(1,11)]

file_list = [path + '0'*(6-len(i)) + i + '.jpg' for i in file_list]



for i in file_list:
	image=Image.open(i)
	image.show()