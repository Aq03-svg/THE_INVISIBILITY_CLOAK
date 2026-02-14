import cv2
import mediapipe as mp
import numpy as np

class HumanSegmenter:
    def __init__(self):
        self.segmenter = mp.solutions.selfie_segmentation.SelfieSegmentation(
            model_selection=1
        )

    def apply(self, frame, background):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.segmenter.process(rgb)

        if result.segmentation_mask is None:
            return frame

        mask = result.segmentation_mask > 0.6

        output = frame.copy()
        output[mask] = background[mask]

        return output