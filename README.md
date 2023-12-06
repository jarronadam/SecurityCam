Security Camera System README

Overview

This Python script implements a basic security camera system using OpenCV. It utilizes your computer's webcam to detect faces and bodies in real-time. When a face or body is detected, the system starts recording and saves the video as an MP4 file. The recording continues for a set duration after the last detection.

Features

Real-Time Detection: 
Uses Haar Cascades to detect faces and bodies in the frame.
Auto-Recording: 
Starts recording automatically upon detection and stops after a predefined time of no detection.
Customizable Settings: Includes settings for detection sensitivity and post-detection recording duration.
Date and Time Stamped: Saves recordings with filenames based on the date and time of recording.

Requirements

Python 3
OpenCV library
Installation
Before running the script, you need to install the OpenCV library. You can install it using pip:

bash
Copy code
pip install opencv-python
Usage
Run the script in a Python environment. The script uses the first available webcam (index 0). You can change the webcam source by modifying the cv2.VideoCapture index.

bash
Copy code
python security_camera.py
Configuration
Video Source: Change the webcam index in cv2.VideoCapture(0) if you have multiple video sources.
Detection Sensitivity: Adjust the scale factor in detectMultiScale method for faces and bodies to change the detection sensitivity.
Post-Detection Recording: Modify SECONDS_TO_RECORD_AFTER_DETEC to change how long the system continues recording after the last detection.
Controls
Press 'q' to quit the program and close the webcam feed.

Notes

The script does not handle scenarios like low light or high-speed movements effectively.
The accuracy of detection may vary based on the quality of the webcam and environmental conditions.
License
This script is provided "as is", without warranty of any kind. You are free to modify and redistribute it.

