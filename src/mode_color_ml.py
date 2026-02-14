import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

import cv2
import numpy as np
from sklearn.cluster import KMeans

def learn_cloak_color(frame, roi):
    x, y, w, h = roi

    if w == 0 or h == 0:
        raise ValueError("Invalid ROI selected")

    # Extract ROI
    roi_img = frame[y:y+h, x:x+w]
    hsv_roi = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)

    pixels = hsv_roi.reshape((-1, 3)).astype(np.float32)

    # If ROI is too uniform, skip KMeans safely
    if np.std(pixels) < 1.0:
        dominant = np.mean(pixels, axis=0)
    else:
        # Add small noise for numerical stability
        pixels += np.random.normal(0, 1, pixels.shape)

        kmeans = KMeans(
            n_clusters=2,
            n_init=10,
            random_state=42
        )
        kmeans.fit(pixels)
        dominant = np.mean(kmeans.cluster_centers_, axis=0)

    h, s, v = dominant

    lower = np.array([max(h-10, 0), max(s-60, 50), max(v-60, 50)], dtype=np.uint8)
    upper = np.array([min(h+10, 180), 255, 255], dtype=np.uint8)

    return lower, upper