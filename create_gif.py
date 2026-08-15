import imageio.v3 as iio


# Put the images in this folder and list them in playback order.
filenames = ["image1.png", "image2.png"]

images = []

for filename in filenames:
    images.append(iio.imread(filename))

# duration is measured in milliseconds; loop=0 repeats forever.
iio.imwrite("my_animation.gif", images, duration=500, loop=0)

print("GIF created: my_animation.gif")
