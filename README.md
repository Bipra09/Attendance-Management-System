# Face Recognition Attendance Management System

Desktop app that marks employee attendance using face recognition. Staff check in with a face scan, and records are saved to CSV and can be exported to Excel.

## Features
- Employee management: add, update, delete, reset, search
- Capture face photo samples via webcam
- Train the face classifier
- Real-time face detection and recognition
- Auto-marked attendance (name, ID, department, time, date, status)
- Attendance report: import/export CSV

## Tech Stack
- Python, Tkinter (GUI)
- OpenCV: Haar Cascade (detection), LBPH (recognition)
- MySQL (employee data)
- Pillow, NumPy

## Project Structure
├── main.py # home screen
├── employee.py # employee CRUD + photo capture
├── train.py # trains LBPH classifier
├── face_recognition.py # live recognition + attendance
├── attendance.py # attendance report (CSV)
├── haarcascade_frontalface_default.xml
├── attend.csv # attendance log
└── data/ # face samples (auto-created)


## Requirements
- Python 3.8+
- MySQL Server
- Webcam

```bash
pip install opencv-contrib-python numpy pillow mysql-connector-python
```

## Setup

**1. Database**
```sql
CREATE DATABASE face_detect;
USE face_detect;
CREATE TABLE employee_data (
  empid INT PRIMARY KEY,
  name VARCHAR(100),
  gender VARCHAR(20),
  phoneno VARCHAR(20),
  email VARCHAR(100),
  `add` VARCHAR(255),
  dept VARCHAR(100),
  post VARCHAR(100),
  ro VARCHAR(100),
  photosample VARCHAR(10)
);
```

**2. Configure**
- Set your MySQL username/password in `employee.py`, `train.py`, `face_recognition.py`
- Replace hardcoded image paths (`C:\Users\...\images\`) with your own `images/` folder

**3. Run**
```bash
python main.py
```

## Usage
1. **Employee Details**: fill in the form → Save → Take Photo Sample
2. **Train Data**: generates `classifier.xml`
3. **Face Detector**: opens webcam and marks attendance on recognition (press `Enter` to exit)
4. **Attendance**: view, import, or export records

## Attendance Format
name, id, department, time, date, status

## Notes
- Train again after adding new employees
- Good lighting improves accuracy
- Each employee is marked once per day
  
## Author 👨‍💻
- [Bipra_Biswas](https://github.com/Bipra09)

## License
MIT

