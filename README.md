
# People Tracking Using YOLO/Kalman Filter and IOU with a Small ONNX Model

![People tracking](https://github.com/FlorianSegard/MLVOT/tree/main/TP4_TP5/tracked_output_video.gif)  
*A comprehensive object tracking program combining multiple methodologies.*

## Project Overview

This project focuses on implementing a robust person-tracking system that maintains consistent IDs for individuals across video frames. The system integrates several components, including:

1. **YOLO (You Only Look Once):** A real-time object detection model to detect people in individual frames.
2. **Kalman Filter:** A state estimation algorithm to predict the next position of detected objects based on motion.
3. **Intersection over Union (IOU):** A metric to associate predicted object positions with actual detections.
4. **Small ONNX Model for Similarity Checking:** A lightweight neural network model to refine tracking by comparing object embeddings for identity consistency.

The integration of these components creates a system capable of handling real-world challenges in object tracking, such as occlusions, reappearances, and ID switching.

---

## Key Features and Components

### 1. **YOLO Object Detection**
- Used to detect people in individual frames.
- Provides bounding boxes and confidence scores for each detected object.
- Lightweight and efficient, suitable for real-time applications.

### 2. **Kalman Filter for Motion Prediction**
- Tracks the state (position and velocity) of detected objects across frames.
- Predicts the next location of each object, reducing dependency on detection in every frame.
- Helps in maintaining object IDs during temporary occlusions.

### 3. **IOU for Detection-to-Track Association**
- Matches detected bounding boxes to predicted boxes based on their overlap ratio.
- Threshold-based matching ensures robust tracking even with slight variations in position.
- Handles cases where multiple objects are in close proximity.

### 4. **Small ONNX Model for Identity Verification**
- A neural network model trained to compare object embeddings.
- Checks the similarity between current and previous detections to ensure ID consistency.
- Adds an additional layer of verification, especially in complex scenarios like overlapping or re-entering objects.

---

## Implementation Details

### Kalman Filter Implementation
The Kalman Filter is implemented to estimate the state of each detected object. Key steps include:
- **State Initialization:** Each detected object is initialized with its position and velocity.
- **Prediction:** The filter predicts the object's position in the next frame based on motion dynamics.
- **Update:** When a new detection matches a prediction (using IOU), the Kalman Filter updates the state with the detection data.

### IOU-Based Matching
- For each predicted bounding box, the IOU is calculated with all detected boxes in the current frame.
- The best match (above a predefined threshold) is used to associate a detection with a track.
- Tracks without matches are updated using the Kalman Filter prediction, and unmatched detections initialize new tracks.

### Integration of the ONNX Model
- The ONNX model refines tracking by comparing feature embeddings of detected objects.
- Each object is assigned an embedding, and cosine similarity is used to compare embeddings across frames.
- This step reduces ID switching and improves tracking performance in challenging scenarios.

---

## Challenges and Solutions

### Challenge 1: Occlusions and Reappearances
- **Solution:** The Kalman Filter predicts object positions during occlusions, allowing tracks to persist temporarily without detections.

### Challenge 2: Overlapping Objects
- **Solution:** IOU ensures that detections are correctly matched to tracks even when objects overlap. The ONNX model adds an additional layer of identity verification.

### Challenge 3: Real-Time Performance
- **Solution:** Optimized YOLO and ONNX models were used, along with efficient Kalman Filter updates, to ensure real-time tracking.

---

## Results
- The system successfully tracks multiple individuals across video frames with minimal ID switches.
- Handles challenging scenarios such as occlusions, reappearances, and overlapping objects.
- Demonstrates high accuracy and efficiency, making it suitable for real-world applications like surveillance and autonomous vehicles.

---

## Conclusion
This project combines state-of-the-art techniques in object detection, motion prediction, and identity verification to create a robust person-tracking system. The integration of a Kalman Filter, IOU-based matching, and a small ONNX model demonstrates how multiple methodologies can be effectively combined to overcome real-world challenges in tracking.
