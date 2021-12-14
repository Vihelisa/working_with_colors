#Imports:
import os 
import cv2
import numpy as np

#variables:
folder = "original_img"
new_folder = "mask_image"
list_img = []

#functions:
def making_new_folder(new_folder_name) -> None:
    if os.path.exists(new_folder_name):
        pass
    else:
        os.mkdir(new_folder_name)
    
#making folder to mask images
making_new_folder(new_folder)

#Take image in the folder
file_names = sorted(os.listdir(folder))
for images in file_names:
    image = os.path.join(folder, images)
    list_img.append(image)

for test_image in list_img:
    #reading the image
    img = cv2.imread(test_image)

    #convert the image to hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #make the mask picture
    mask = cv2.inRange(hsv, (20, 25, 25), (100, 255,255))

    ## slice the green
    imask = mask>0
    green = np.zeros_like(img, np.uint8)
    green[imask] = img[imask]

    ## save 
    new_image = test_image.replace(folder, new_folder)
    cv2.imwrite(new_image, green)