import imageio.v3 as iio
from PIL import Image

filenames = ['nyan-cat1.png', 'nyan-cat2.png', 'nyan-cat3.png']
images = []

# Resize all images to the same size
first_image = Image.open(filenames[0])
target_size = first_image.size  # Get the size of the first image

for filename in filenames:
    img = Image.open(filename).convert("RGBA")  # Ensure uniform mode
    img = img.resize(target_size)  # Resize to the first image's size
    images.append(img)  # Append PIL image directly

# Save as GIF using PIL
images[0].save("cat.gif", save_all=True, append_images=images[1:], duration=500, loop=0)