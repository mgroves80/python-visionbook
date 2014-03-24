__author__ = 'sunyguy01'

from PIL import Image
from pylab import *

#Convert to grayscale
pil_im = Image.open('sb-104.jpeg').convert('L')

pil_im.save('sb-104-gray.jpg')

#Thumbnail
pil_im = Image.open('sb-104.jpeg')

pil_im.thumbnail((100, 100))

pil_im.save('sb-104-thumbnail.jpg')

#Crop and Paste
pil_im = Image.open('sb-104.jpeg')

cropbox = (0, 0, 100, 200)

region = pil_im.crop(cropbox)

region = region.transpose(Image.ROTATE_90)

newCropBox = (0, 0, 200, 100)

pil_im.paste(region, newCropBox)

pil_im.save('sb-104-cropandpaste.jpg')

#Resize and rotate
pil_im = Image.open('sb-104.jpeg')

pil_im = pil_im.resize((2000, 1000))
pil_im = pil_im.rotate(90)

pil_im.save('sb-104-resizeandrotate.jpg')

#matplotlib
#read image into array
im = array(Image.open('sb-104.jpeg'))

#plot the image
imshow(im)

x = [600,775]
y = [221,216]

#plot the points with red star-markers

#draw line connect first 2 points
plot(x, y, 'r*-')

title('Plotting line between Wilson and Lynch')

show()

#histogram
im = array(Image.open('sb-104.jpeg').convert('L'))

#create a new figure
figure()
#don't use colors
gray()
#show contours with origin upper left corner
contour(im, origin='image')
axis('equal')
axis('off')

#create and show histogram
figure()
hist(im.flatten(), 128)

print im.flatten()
show()

