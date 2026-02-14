import cv2
from utils.camera import get_camera
from utils.background import capture_background
from mode_color_ml import learn_cloak_color

cap = get_camera()
background = capture_background(cap)

print("INFO: Webcam started")
print("INFO: Press 'c' to capture cloak color")
print("INFO: Press 'q' to quit")

lower, upper = None, None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.putText(
        frame,
        "Press 'c' to select cloak | Press 'q' to quit",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("THE INVISIBILITY CLOAK - SETUP", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        roi = cv2.selectROI("Select Cloak Region", frame, False)
        cv2.destroyWindow("Select Cloak Region")
        lower, upper = learn_cloak_color(frame, roi)
        print("Cloak color learned successfully!")
        break

    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        exit()

# -------- MAIN CLOAK LOOP --------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, None)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, None)

    cloak = cv2.bitwise_and(background, background, mask=mask)
    rest = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask))
    output = cloak + rest

    cv2.putText(
        output,
        "Mode: ML Color | Press Q to quit",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("THE INVISIBILITY CLOAK", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()