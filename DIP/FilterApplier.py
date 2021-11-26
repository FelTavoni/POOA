# Importing all necessary libraries
import os
import cv2
import numpy as np
import FilterStrategies

class FilterApplier:

    def __init__(self, strategy: object = None):
        self.setStrategy(FilterStrategies.Strategy)
    
    def setStrategy(self, strategy: object) -> None:
        self._strategy = strategy

    # Selects the right strategy based on a string
    def strategySelector(self, filter: str) -> None:
        if filter == "grayscale":
            self.setStrategy(FilterStrategies.Grayscale())
        elif filter == "sharpen":
            self.setStrategy(FilterStrategies.Sharpen())
        elif filter == "sepia":
            self.setStrategy(FilterStrategies.Sepia())
        elif filter == "sketch":
            self.setStrategy(FilterStrategies.Sketch())
        elif filter == "sketch_colored":
            self.setStrategy(FilterStrategies.Sketch_Colored())
        elif filter == "invert":
            self.setStrategy(FilterStrategies.Invert())
        elif filter == "summer":
            self.setStrategy(FilterStrategies.Summer())
        elif filter == "winter":
            self.setStrategy(FilterStrategies.Winter())
        else:
            self.setStrategy(None)

    # Apply the filter to the image
    def applyFilter(self, picture: np.array, filter: str) -> np.array:

        self.strategySelector(filter)
        try:
            picture = self._strategy.execute(picture)
        except Exception as e:
            # raise e
            print("The selected option is not unavailable or is written wrong!")

        return picture.copy()

    pass