from PIL import Image
import numpy as np
from os import listdir

input_dir = "/Users/admin/Desktop/DataSet"

directories = listdir(input_dir)
variable = []
for folder in directories:
    if folder != ".DS_Store":
        folder2 = listdir(input_dir + '/' + folder)
        for image in folder2:
         if image == ".DS_Store":
            pass
         else:
            im = Image.open(input_dir+"/"+folder+"/"+image) #Opening image
            im = (np.array(im)) #Converting to numpy array
            r = im[:,:,0].flatten() #Slicing to get R data
            g = im[:,:,1].flatten() #Slicing to get G data
            b = im[:,:,2].flatten()
            label = [folder]
            variable=np.append(variable,np.array(list(label) + list(r) + list(g) + list(b),np.uint8))

print variable
out = np.array(variable,np.uint8)
out.tofile("out.bin")
