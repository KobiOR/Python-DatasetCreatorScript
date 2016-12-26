from PIL import Image
import numpy as np
from os import listdir

input_dir = "/Users/admin/Desktop/DataSet"  # Folders should be arranged hierarchically order

directories = listdir(input_dir)
variable = []
size = 32, 32
for folder in directories:
    if folder != ".DS_Store":
        folder2 = listdir(input_dir + '/' + folder)
        for image in folder2:
            if image == ".DS_Store":
                pass
            else:
                im = Image.open(input_dir + "/" + folder + "/" + image)
                print im.size
                im_resized = im.resize(size, Image.ANTIALIAS)
                im_resized.save(image, "jpeg")# Opening image
                im_resized = (np.array(im_resized))  # Converting to numpy array
                # Note! Flatten [flatten()] function Return a copy of the array collapsed into one dimension.
                r = im_resized[:, :, 0].flatten()  # Slicing to get R data
                g = im_resized[:, :, 1].flatten()  # Slicing to get G data
                b = im_resized[:, :, 2].flatten()  # Slicing to get B data
                label = [folder]  # Sets the folder name as a label of the image
                variable = np.append(variable, np.array(list(label) + list(r) + list(g) + list(b), np.uint8))

print variable
out = np.array(variable, np.uint8)
out.tofile("out.bin")
