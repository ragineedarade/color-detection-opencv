 import cv2
import numpy as np

# Define your colors and their HSV ranges (you can tweak these)

color_defs = [
    {"name": "Red",    "ranges": [([0, 120, 70],   [5, 255, 255]),
                                  ([175, 120, 70], [180, 255, 255])]},
    {"name": "Orange", "ranges": [([6, 100, 100],  [15, 255, 255])]},
    {"name": "Yellow", "ranges": [([16, 100, 100], [35, 255, 255])]},
    {"name": "Green",  "ranges": [([36,  50,  50], [85, 255, 255])]},
    {"name": "Sky Blue", "ranges": [
        ([86, 30, 100], [100, 150, 255])]},  # Light cyan sky
    {"name": "Blue",   "ranges": [([101, 100, 100], [125, 255, 255])]},
    {"name": "Purple", "ranges": [([126, 100, 100], [160, 255, 255])]},
    {"name": "Pink",   "ranges": [([161, 100, 100], [174, 255, 255])]},
    {"name": "Brown",  "ranges": [([10, 100, 20],   [20, 255, 200])]},
    {"name": "Cyan",   "ranges": [([80, 100, 100],  [100, 255, 255])]},
    {"name": "Gold",   "ranges": [([20, 150, 150],  [30, 255, 255])]},
    # {"name": "Gray",   "ranges": [([0, 0, 40],      [180, 40, 200])]},
    {"name": "Black",  "ranges": [([0, 0, 0],       [180, 255, 30])]},
    {"name": "White",  "ranges": [([0, 0, 200],     [180, 30, 255])]},
    {"name": "Skin",   "ranges": [([0, 48, 80],     [20, 255, 255])]},
]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # For each color, build a mask (combining sub-ranges if needed), find contours and label them
    for c in color_defs:
        # combine all sub-ranges for this color into one mask
        mask = None
        for (low, high) in c["ranges"]:
            low_np, high_np = np.array(low), np.array(high)
            m = cv2.inRange(hsv, low_np, high_np)
            mask = m if mask is None else cv2.bitwise_or(mask, m)

        # find all contours for this color
        contours, _ = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) < 800:
                continue
            x, y, w, h = cv2.boundingRect(cnt)
            # draw box + label
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)
            cv2.putText(frame, c["name"], (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Multi-Color Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
