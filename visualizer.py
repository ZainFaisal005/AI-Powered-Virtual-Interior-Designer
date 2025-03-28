# visualizer.py

import cv2
import numpy as np

def visualize_design(image_path):
    image = cv2.imread(image_path)
    
    # Create a 3D effect by tilting the image
    rows, cols, _ = image.shape
    matrix = cv2.getRotationMatrix2D((cols/2, rows/2), -15, 1)
    tilted_image = cv2.warpAffine(image, matrix, (cols, rows))
    
    # Display the image
    cv2.imshow('3D Visualization', tilted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
