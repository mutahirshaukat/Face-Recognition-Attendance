# Face-Recognition-Attendance
The Facial Recognition Attendance System automates attendance tracking using real-time computer vision. It identifies individuals via a webcam feed by comparing face encodings and instantly logs their presence with timestamps into a CSV file. This project eliminates manual marking errors, ensuring accurate and efficient management.

## Introduction
The Facial Recognition Attendance System automates attendance tracking through real-time facial recognition technology. By leveraging computer vision algorithms, it identifies individuals from a webcam feed, logs their attendance with timestamps, and eliminates manual marking.

## Objective
The objective of the Facial Recognition Attendance System is to automate and modernize the attendance management process.Eliminate manual attendance marking, reducing administrative workload.
Provide accurate and real-time attendance tracking.
Enhance efficiency and productivity in attendance management.

## How It Gonna Work
flowchart.jpg

## Algorithm
01. Initialize video capture from the webcam.
02. Load known face encodings and names from images.
03. Create lists of all students and present students.
04. Create a CSV file for the current date.
05. Capture frames from the video feed
06. Resize frames, detect and encode faces.
07. Compare faces, recognize and draw rectangles.
08. Record attendance for recognized faces.
09. Display real-time video feed with attendance status.

## Use of Libraries
01. face_recognition:
      Purpose: Detects and recognizes faces.
      Functionality: Provides simple methods to load images, detect face locations, and extract face encodings.
02. cv2 (OpenCV):
      Purpose: Captures video from the webcam and processes images.
      Functionality: Handles real-time video streaming, image resizing, drawing shapes, and adding text to images.
03. numpy:
      Purpose: Performs numerical operations, especially with arrays.
      Functionality: Supports efficient manipulation and comparison of face encodings.
04. csv:
      Purpose: Writes attendance records to a CSV file.
      Functionality: Enables creation, writing, and manipulation of CSV files for storing attendance data.
05. datetime:
      Purpose: Manages date and time operations.
      Functionality: Retrieves and formats the current date and time for timestamping attendance records.
06. os:
      Purpose: Interacts with the operating system.
      Functionality: Handles directory and file operations, such as listing image files in a directory and joining file paths.
