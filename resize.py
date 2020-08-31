import cv2
import numpy as np
import sys
import os
import fnmatch


def sharp(image):
    kernel = np.array([[0,-1,0], [-1, 5, -1], [0 ,-1, 0]])
    new_image = cv2.filter2D(image, -1, kernel)
    cv2.imshow("Sharpened", new_image)
    cv2.waitKey(0)
    return new_image

def blur(image):
    kernels = [3, 7, 9, 13]
    for idx, k in enumerate(kernels):
        blur_img = cv2.blur(image, (k,k))
        cv2.imshow(str(k), blur_img)
        cv2.waitKey(0)
    return

def resize(fname, width, height):

    image = cv2.imread(fname)
    cv2.imshow('Original image', image)
    cv2.waitKey(0)

    org_height, org_width = image.shape[0:2]
    if org_width >= org_height:
        new_image = cv2.resize(image, (width, height))
    else:
        new_image = cv2.resize(image, (height, width))
    return fname, new_image

# file_name, new_image = resize('amuu.png', 1280, 960)
# cv2.imshow('new resized', new_image)
# cv2.waitKey(0)

#blur(new_image)

#image = sharp(new_image)

listOfFiles = os.listdir('.')
pattern = "*.png"

width = 1200 
height = 960

if not os.path.exists('new_folder'):
    os.makedirs('new_folder')

for filename in listOfFiles:
    if fnmatch.fnmatch(filename, pattern):
        filename, new_image = resize(filename, width, height)
        cv2.imwrite("new_folder\\"+ filename, new_image)