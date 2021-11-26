import os
import sys
import cv2
import numpy as np
import FilterApplier

if __name__ == "__main__":

    # Instanciate filter applier object
    filterApplier = FilterApplier.FilterApplier()

    # Collect program params and calls 'applyFilter', writing the result
    picture = cv2.imread(sys.argv[1])
    filter = sys.argv[2]
    picture = filterApplier.applyFilter(picture, filter)
    cv2.imwrite(os.path.join('.', 'Image.jpg'), picture)