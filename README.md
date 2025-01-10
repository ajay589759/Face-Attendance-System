# Face-Attendance-System

This project is a Face Recognition-based Attendance System that automates the process of marking attendance using facial recognition technology. The system uses OpenCV for face detection, Tkinter for the GUI, and MySQL to store attendance records. It ensures accuracy and prevents duplicate attendance for the same individual within a session.

**Features**
Face Detection and Recognition: Utilizes OpenCV's Haar Cascade classifiers to detect and recognize faces in real-time.
Attendance Marking: Automatically marks attendance in the database upon successful recognition.
Duplicate Prevention: Ensures that a student’s attendance is not marked more than once in the same session.
User-Friendly GUI: Built using Tkinter for easy navigation and operation.
Database Integration: Stores attendance records in a MySQL database for future reference.
**Technologies Used**
Programming Language: Python
**Libraries:**
OpenCV: For face detection and recognition
Tkinter: For GUI development
Database: MySQL
How to Use
**Setup the Database:**

Create a MySQL database and table for storing attendance.
Configure the database connection in the code.
**Add Student Data:**

Add student information (ID, roll number, name, etc.) into the database.
**Run the Application:**

Execute the Python script to launch the GUI.
Use the camera to capture and recognize faces for marking attendance.
Folder Structure
**/Dataset:** Contains face images for training the recognition model.
**/Attendance: **Stores attendance records (if saved locally).
**face_recognition.py:** Main script for face recognition and attendance marking.
**train_model.py:** Script to train the facial recognition model.
Future Enhancements
Integration with cloud-based databases for scalability.
Adding support for multiple sessions or classes.
Enhancing accuracy with advanced face recognition algorithms like deep learning models.
Implementing real-time notifications for attendance updates.

Feel free to contribute or raise issues to improve the system!
