# Personal-Project---Detection-of-a-fatigue-for-a-car-driver-AI-model

This project implements driver drowsiness detection using YOLOv5 for face and eye detection, combined with a deep learning model to classify eye states (open or closed). When signs of fatigue are detected, an alert system is triggered to prevent accidents.

Technologies & Tools Used

Deep Learning Frameworks: TensorFlow, PyTorch
Computer Vision: OpenCV, YOLOv5
Firmware Programming : Python
Libraries: NumPy, Pygame (for audio alerts)
Hardware: GPU (for training)

Model Design & Implementation : 

Data Collection & Preprocessing

Used an open dataset of labeled eye images (open vs closed)

Augmented the dataset (flipping, brightness changes, noise)

Normalized and resized images for efficient training


Model Architecture : 

YOLOv5 → Detects face and eyes in real-time

CNN (Custom Model / Pretrained) → Classifies eye state (open/closed)


Training the Model : 

 YOLOv5 training for face & eye detection
 
 CNN training using Cross-Entropy Loss + Adam Optimizer
 
 Evaluation Metrics: Accuracy, Precision, Recall
 

Real-Time Implementation : 


YOLOv5 detects the driver’s face & eyes

CNN Model predicts whether eyes are open/closed

Score-based Alert System → If eyes are closed for multiple frames, an alarm is triggered

