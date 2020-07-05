import cv2
import pydicom
import os
import pylab
import dicom
import numpy as np
from pydicom.pixel_data_handlers.util import convert_color_space

file = 'large.dcm'

read_dcm_file = pydicom.dcmread(file)

img_arr = read_dcm_file.pixel_array

shape = img_arr.shape
image_2d = img_arr.astype(float)

dimention = 0
if len(shape) == 4:
    dimension = shape[1]
    mid_frame = int(float(img_arr.shape[0]) / 2)
    if img_arr.shape[3] == 3:
        print(img_arr[mid_frame].shape)
        imgexc_render = convert_color_space(img_arr[mid_frame], 'RGB', 'RGB')
    image_2d = imgexc_render.astype(float)
else:
    dimension = shape[0]

if dimension > 512 :
    image_2d_scaled = 255 - (np.maximum(image_2d,0) / image_2d.max() * 255.0)
else :
    level = 600
    window = 1600
    if len(shape) == 4:
        image_2d_scaled = (np.maximum(image_2d,0) / image_2d.max() * 255.0)
    else : 
        image_2d_scaled = np.piecewise(image_2d, 
                        [image_2d <= (level - 0.5 - (window-1)/2),
                            image_2d > (level - 0.5 + (window-1)/2)],
                                [0, 255, lambda image_2d: ((image_2d - (level - 0.5))/(window-1) + 0.5)*(255-0)])

image_2d_scaled = np.uint8(image_2d_scaled)

cv2.imwrite('result.jpg', image_2d_scaled)