import cv2

def get_camera():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    if not cap.isOpened():
        raise RuntimeError("❌ Cannot access webcam")
    return cap