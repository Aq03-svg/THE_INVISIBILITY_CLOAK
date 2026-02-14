# 🧙‍♂️ THE INVISIBILITY CLOAK — Mode 1

An **ML-based adaptive invisibility cloak** implemented using Python, OpenCV, and scikit-learn.  
This project recreates the invisibility cloak illusion by **learning the cloak color dynamically** from a user-selected region and replacing it with the background in real time.

---

## 📌 Project Overview

Traditional invisibility cloak implementations rely on **hardcoded color thresholds** (e.g., red cloak), which fail under varying lighting conditions.  
This project improves robustness by using **Machine Learning (K-Means clustering)** to automatically learn the cloak color from the video feed.

The system operates in real time using a webcam and adapts to different cloak colors and lighting environments.

---

## 🧠 Key Concept: ML-Based Adaptive Color Cloak

- The user selects a **Region of Interest (ROI)** corresponding to the cloak
- **Unsupervised learning (K-Means)** is applied to learn the dominant cloak color
- Dynamic HSV thresholds are generated from the learned color
- Cloak pixels are replaced with a pre-captured background
- Result: a convincing invisibility illusion

---

## ✨ Features

- Real-time webcam processing
- ROI-based cloak color selection
- ML-based adaptive color learning (K-Means)
- Robust to lighting variations
- Clean modular code structure
- macOS-compatible camera handling

---

## 🛠️ Tech Stack

- **Python 3.10**
- **OpenCV**
- **NumPy**
- **scikit-learn**
- macOS AVFoundation backend

---

## 📂 Project Structure
'''

THE_INVISIBILITY_CLOAK/
│
├── src/                            # All source code
│   │
│   ├── main.py                     # Entry point (mode selector & pipeline)
│   │
│   ├── mode_color_ml.py            # Mode 1: ML-based adaptive color cloak
│   │
│   ├── mode_segmentation.py        # Mode 2: Human segmentation cloak (future)
│   │
│   └── utils/                      # Reusable helper modules
│       │
│       ├── camera.py               # Webcam initialization & handling
│       ├── background.py           # Background capture logic
│       └── __init__.py             # Makes utils a package
│
├── demo_output/                    # Screenshots / demo GIFs (optional)
│
├── requirements.txt                # Python dependencies
│
├── README.md                       # Project documentation
│
├── .gitignore                      # Files/folders ignored by Git
│
└── venv/                           # Virtual environment (NOT pushed)
'''