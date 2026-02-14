## 🔍 Project Overview

This project implements a **dual-mode invisibility cloak system** using computer vision and machine learning techniques.

- **Mode 1:** An **ML-based adaptive color cloak** that uses **K-Means clustering** to dynamically learn the cloak color from a user-selected region of interest (ROI).
- **Mode 2:** A **deep-learning-based human segmentation cloak** implemented using **MediaPipe**, where a pretrained segmentation model identifies human pixels and replaces them with the background in real time.

The segmentation mode leverages **TensorFlow Lite** and **Metal acceleration on Apple Silicon**, enabling efficient real-time performance without requiring model training.


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
```

THE_INVISIBILITY_CLOAK/
│
├── demo_output/                     # Screenshots / demo GIFs (optional)
│
├── src/                             # Source code
│   │
│   ├── main.py                      # Entry point (mode selector & pipeline)
│   │
│   ├── mode_color_ml.py             # Mode 1: ML-based adaptive color cloak
│   │
│   ├── mode_segmentation.py         # Mode 2: Human segmentation cloak
│   │
│   ├── baseline_invisibility_cloak.py
│   │                                # Baseline OpenCV-only implementation
│   │
│   ├── utils/                       # Reusable helper modules
│   │   ├── camera.py                # Webcam initialization & handling
│   │   ├── background.py            # Background capture logic
│   │   └── __pycache__/             # Python cache (NOT pushed)
│   │
│   └── __pycache__/                 # Python cache (NOT pushed)
│
├── venv/                            # Virtual environment (NOT pushed)
│   ├── bin/
│   ├── include/
│   ├── lib/
│   ├── share/
│   └── pyvenv.cfg
│
├── requirements.txt                 # Python dependencies
│
├── README.md                        # Project documentation
│
└── .gitignore                       # Git ignore rules

```
## 🧠 Mode 2: Human Segmentation Invisibility Cloak (Deep Learning)

Mode 2 removes the dependency on cloak color entirely by using **deep-learning-based human segmentation**.  
Instead of detecting a specific color, the system identifies **human pixels** and replaces them with the captured background in real time.

---

### 🔍 How It Works

- A **pretrained human segmentation model (MediaPipe Selfie Segmentation)** is used
- Each video frame is processed to obtain a **pixel-wise human mask**
- Pixels classified as *human* are replaced with the background
- The result is a **color-independent invisibility effect**

This approach works regardless of clothing color or texture.

---

### ✨ Key Features

- Deep-learning-based semantic segmentation
- Color-independent invisibility
- Real-time performance
- Uses pretrained model (no training required)
- GPU / Metal acceleration on Apple Silicon

---

### 🧪 Execution Flow

1. Background is captured
2. Webcam feed starts
3. Human segmentation mask is generated per frame
4. Human pixels are replaced with background
5. Invisibility illusion is displayed in real time

---

### ⚙️ Technology Used

- MediaPipe Selfie Segmentation
- TensorFlow Lite (XNNPACK delegate)
- OpenCV for video processing
- Python 3.10

---

### 📊 Mode Comparison

| Feature | Mode 1 (ML Color Cloak) | Mode 2 (Segmentation Cloak) |
|------|--------------------------|-----------------------------|
| Technique | K-Means Clustering | Deep Learning |
| Dependency | Cloak color | Human presence |
| Lighting robustness | Medium | High |
| Clothing color | Limited | Any |
| Computational cost | Low | Moderate |

---

### 📌 Note

Mode 2 complements Mode 1 by providing a **more robust and general invisibility solution**, demonstrating the use of both **classical machine learning** and **deep learning** approaches within the same system.