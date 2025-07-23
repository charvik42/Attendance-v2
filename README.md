# Face Recognition Attendance System

This is a Python-based real-time face recognition system for marking attendance using a webcam. The system supports saving attendance data in:
- CSV
- MySQL database (via Workbench)

It uses `OpenCV`, `face_recognition`, and `pymysql`.

---

## Features

- Live webcam face recognition
- Encodes and stores known faces
- New face registration on-the-fly
- Attendance marked with name, time, and date
- Data saved to `.csv` or MySQL
- Prevents duplicate entries per day

---

## Requirements
Install Python dependencies using the command `pip install -r requirements.txt` in your terminal.
Use MySQL Workbench and run the script `Attendance Data.sql`. 
Make sure to set the password and database to your own. 
