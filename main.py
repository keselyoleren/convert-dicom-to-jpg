import cv2
import pydicom
import os

file = 'img1.dcm'

ds = pydicom.read_file(file)
img = ds.pixel_array

scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv2.resize(img, dim)

print(dim)

cv2.imwrite('result.jpg', resized)