#P10 data extraction
import cv2 
import numpy as np 
from matplotlib import pyplot as plt
#import pytesseract
import os

template_path = "data/img/template/20230214_131608.jpg"
raw_images_path = "data/img/monthly/august/20230214_132258.jpg"
img_ref = cv2.imread(template_path)

def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)
    h, w, d = im_data.shape 

    # whot size does the figure need to be?
    figsize = w/float(dpi), h/float(dpi)
    # Create a figure of the right size with one axes
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0,0,1,1])
    #Hides spines, ticks, etc
    ax.axis('off')

    # Display the Image 
    ax.imshow(im_data, cmap='gray')
    plt.show()

def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h,w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

invert_img = cv2.bitwise_not(img_ref)
cv2.imwrite("data/img/template/temp/inverted_template.jpg", invert_img)
display("data/img/template/temp/inverted_template.jpg")
