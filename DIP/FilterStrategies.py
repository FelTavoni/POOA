import os
import cv2
import random
import imutils
import numpy as np
from abc import ABC, abstractmethod
from scipy.interpolate import UnivariateSpline

# Filters implementations were based on the following website
# https://www.analyticsvidhya.com/blog/2021/07/an-interesting-opencv-application-creating-filters-like-instagram-and-picsart/

class Strategy(ABC):
    @abstractmethod
    def execute(self, picture: np.array) -> np.array:
        return picture

    pass

class Grayscale(Strategy):

    def execute(self, picture: np.array) -> np.array:
        return cv2.cvtColor(picture, cv2.COLOR_RGB2GRAY)

    pass

class Sharpen(Strategy):

    def execute(self, picture: np.array) -> np.array:
        kernel = np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
        return cv2.filter2D(src = picture, ddepth = cv2.CV_16U, kernel = kernel)

    pass

class Sepia(Strategy):

    def execute(self, picture: np.array) -> np.array:
        # Converting to float to prevent loss
        picture = np.array(picture, dtype=np.float64)
         # multipying image with special sepia matrix
        picture = cv2.transform(picture, np.matrix([[0.272, 0.534, 0.131],
                                                    [0.349, 0.686, 0.168],
                                                    [0.393, 0.769, 0.189]]))
        # normalizing values greater than 255 to 255
        picture[np.where(picture > 255)] = 255
        picture = np.array(picture, dtype=np.uint8)
        return picture

    pass

class Sketch(Strategy):

    def execute(self, picture: np.array) -> np.array:
        picture, _ = cv2.pencilSketch(picture, sigma_s = 60, sigma_r = 0.07, shade_factor = 0.1) 
        return  picture

    pass

class Sketch_Colored(Strategy):

    def execute(self, picture: np.array) -> np.array:
        _, picture = cv2.pencilSketch(picture, sigma_s = 60, sigma_r = 0.07, shade_factor = 0.1) 
        return  picture

    pass

class Invert(Strategy):

    def execute(self, picture: np.array) -> np.array:
        return  cv2.bitwise_not(picture)

    pass

def LookupTable(x, y):
    spline = UnivariateSpline(x, y)
    return spline(range(256))

class Summer(Strategy):

    def execute(self, picture: np.array) -> np.array:
        increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel, red_channel = cv2.split(picture)
        red_channel = cv2.LUT(red_channel, increaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, decreaseLookupTable).astype(np.uint8)
        return cv2.merge((blue_channel, green_channel, red_channel))

    pass

class Winter(Strategy):

    def execute(self, picture: np.array) -> np.array:
        increaseLookupTable = LookupTable([0, 64, 128, 256], [0, 80, 160, 256])
        decreaseLookupTable = LookupTable([0, 64, 128, 256], [0, 50, 100, 256])
        blue_channel, green_channel, red_channel = cv2.split(picture)
        red_channel = cv2.LUT(red_channel, decreaseLookupTable).astype(np.uint8)
        blue_channel = cv2.LUT(blue_channel, increaseLookupTable).astype(np.uint8)
        return cv2.merge((blue_channel, green_channel, red_channel))

    pass