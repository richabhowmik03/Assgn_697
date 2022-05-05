from PIL import Image
import os

# imported the os library to open files from the present directory

newsize = (300, 300)  # setting the new size

#FOR QUESTION NO.1
for im in os.listdir('.'):  # to load all the images at once
    if im.endswith('jpeg'):
        i = Image.open(im)
        i.show()


#for question no. 2
for im in os.listdir('.'):  # the first for loop has been used to list out the type of the images
    name, extension = os.path.splitext(im)
    print(extension)
for im in os.listdir('.'):  # the second for loop has been used to open the image files
    if im.endswith('jpeg'):
        i = Image.open(im)
        width, height = i.size   # the size of the image has been expressed in terms of width and height
        print(f"The size of the image is expressed in terms of width: {width} and height: {height}")


#For question no. 3
for im in os.listdir('.'):  # the first for loop has been used to list out the type of the images
    if im.endswith('jpeg'):
        i = Image.open(im)
        width, height = i.size  # the size of the image has been expressed in terms of width and height
        # up to this what we are doing is getting the size of the images
        # but our purpose is to crop the images,
        # so we are going to use the crop method which takes four arguments
        i2 = i.crop((250, 20, width-150, height-150))  # crop method has been used to crop the images
        i2.show()

#for question no.4
for im in os.listdir('.'):  # the first for loop has been used to list out the type of the images
    if im.endswith('jpeg'):
        i = Image.open(im)
        width, height = i.size  # the size of the image has been expressed in terms of width and height
        # up to this what we are doing is getting the size of the images
        # but we have to resize images
        # by using resize method we are resizing the images
        i2 = i.resize(newsize)
        i2.show()

#for question no.5
car = Image.open('car.jpeg')
flip_car = car.transpose(Image.FLIP_TOP_BOTTOM) # for flipping the image vertically
flip_car.show()

mountain = Image.open('mountain.jpeg')
rotate_mountain = mountain.transpose(Image.ROTATE_90) #for rotating the image by 90 degree
rotate_mountain.show()

bike = Image.open('bike.jpeg')
flip_bike = bike.transpose(Image.FLIP_LEFT_RIGHT) #For flipping horizontally
flip_bike.show()
