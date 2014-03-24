__author__ = 'sunyguy01'

from PIL import Image
from pylab import *

#Interactive Annotations
im = array(Image.open('sb-104.jpeg'))

imshow(im)

print 'Please click 3 points'

inputs = ginput(3)

print 'you clicked:'
print inputs

x = []
y = []

for pt in inputs:
    print 'plotting point: [%d,%d]' % (pt)
    x.append(pt[0])
    y.append(pt[1])

plot(x, y, 'y*')
ylim([501, 0])
xlim([0, 958])
draw()

show()