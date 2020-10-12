'''
We're going to install the pip install pillow library
It is a fork of the PIL (Python Imaging Library) with easy to use function calls
'''

from PIL import Image

mac = Image.open('example.jpg')

# print(type(mac))  will give you <class 'PIL.JpegImagePlugin.JpegImageFile'>

#mac.show()
mac.size  #(1993, 1257)
mac.filename
mac.format_description


'''
CROPPING IMAGES
'''

mac.crop((0,0,100,100))

pencils = Image.open('pencils.jpg')
print(pencils.size)   # (1950, 1300)

x = 0
y = 0

w = 1950 / 3
h = 1300 / 10

cropped_pencils_1 = pencils.crop((x,y,w,h))
# cropped_pencils_1.show()

x2 = 0
y2 = 1100

w2 = 1950 / 3
h2 = 1300

cropped_pencils_2 = pencils.crop((x2,y2,w2,h2))
# cropped_pencils_2.show()



mac_halfway = 1993 / 2
x3 = mac_halfway - 200
w3 = mac_halfway + 200

y3 = 800
h3 = 1275

mac_computer = mac.crop((x3,y3,w3,h3))
# mac_computer.show()

'''
COPYING AND PASTING IMAGES
'''

computer = mac.crop((x3,y3,w3,h3))
mac.paste(im=computer, box=(0,0))
# mac.show()  # will have another mac pasted on the top left corner of the image | IT PERMANENTLY AFFECTS THE VARIABLE


# You can also resize an image
mac.resize((3000,5000))

# You can rotate images
mac.rotate(90)

'''
COLOUR TRANSPARENCY    RGBA - RED, GREEN, BLUE, ALPHA     

All values range from 0 - 255
For alpha, if the value is 0 then image is transparent, if its 255, the image is opaque
'''

red = Image.open('red_color.jpg')
blue = Image.open('blue_color.png')

#blue.putalpha(0) # image will be completely transparent, so you're only see while
#blue.putalpha(255) # image will be completely opaque, so you will see blue

blue.putalpha(128)
red.putalpha(128)


blue.paste(im=red, box=(0,0), mask=red)


'''
SAVE IMAGE
'''

#blue.save('black.jpg')