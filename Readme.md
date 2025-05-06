# 🎨 Color Detection with Python & OpenCV

This project demonstrates **real-time color detection** using Python and OpenCV. The camera feed is processed to detect and highlight specific colors using HSV color space.

[![Watch the video](https://img.youtube.com/vi/aFNDh5k3SjU/0.jpg)](https://www.youtube.com/watch?v=aFNDh5k3SjU)

---

## 🚀 Features

- Access webcam using OpenCV
- Convert frames to HSV color space
- Real-time color masking
- Easy to customize for different colors

---

## 📦 Requirements

- Python 3.x
- OpenCV (`pip install opencv-python`)

---

## 📂 File Structure

color-detection-opencv/
│
├── color_detection.py # Main Python file for color detection
├── README.md # This file


---

## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/color-detection-opencv.git
   cd color-detection-opencv

Install dependencies:

bash
Copy
Edit
pip install opencv-python
Run the script:

bash
Copy
Edit
python color_detection.py
Press q to quit the video window.

🎥 Sample Output


🛠 Customization
Edit the HSV range in the Python file to detect different colors:

python
Copy
Edit
lower = np.array([H_min, S_min, V_min])
upper = np.array([H_max, S_max, V_max])
📺 Video Tutorial
Check out the video guide here:
📹 https://www.youtube.com/watch?v=aFNDh5k3SjU

