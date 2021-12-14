#imports:
#from PIL import Image
import numpy as np
import cv2
import os
from matplotlib.pyplot import imshow

#variables:
folder = "original_img"
new_folder = "mask_image"
list_img = []

def making_new_folder(new_folder_name) -> None:
    if os.path.exists(new_folder_name):
        pass
    else:
        os.mkdir(new_folder_name)

making_new_folder(new_folder)
#Take image in the folder
file_names = sorted(os.listdir(folder))
for images in file_names:
    image = os.path.join(folder, images)
    list_img.append(image)

test_image = list_img[1]
#print(test_image)

img = cv2.imread(test_image)
soma = (img[:,:,0] + img[:,:,1] + img[:,:,2])
r = img[:,:,2]
g = img[:,:,1]
b = img[:,:,0]

r1 = np.divide(r, soma, out=np.zeros_like(r, dtype=np.float64), where=soma!=0)
b1 = np.divide(b, soma, out=np.zeros_like(b, dtype=np.float64), where=soma!=0)
g1 = np.divide(g, soma, out=np.zeros_like(g, dtype=np.float64), where=soma!=0)

exG =(2*g1) - r1 - b1 #se mudar o numero que multiplica o g1, a foto fica com tons de roxo e azul, independente da mudança feita
imshow(exG)
mini = exG.min()
maxi = exG.max()
#print(mini, maxi)
#print(type(exG))

_, exG1 = cv2.threshold(exG, 0.2, 1055, cv2.THRESH_BINARY) #(_,)=> quer dizer que vc quer ignorar o primeiro valor da tupla que ele está retornando
imshow(exG1)

