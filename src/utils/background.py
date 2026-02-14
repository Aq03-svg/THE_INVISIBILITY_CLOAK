import numpy as np
import cv2
import time

def capture_background(cap, frames=30):
    bg = None
    time.sleep(2)
    for _ in range(frames):
        ret, frame = cap.read()
        if ret:
            bg = frame
    if bg is None:
        raise RuntimeError("Failed to capture background")
    return np.flip(bg, axis=1)