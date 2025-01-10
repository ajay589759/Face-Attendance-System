# import cv2
# from tkinter import *
# from PIL import Image, ImageTk
# import mysql.connector
# from datetime import datetime
#
#
# class Face_Recognition:
#
#     def __init__(self, root, conn):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition Panel")
#         self.conn = conn
#
#         # This part is image labels setting start
#         # first header image
#         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
#         img = img.resize((1366, 130), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)
#
#         # set image as label
#         f_lb1 = Label(self.root, image=self.photoimg)
#         f_lb1.place(x=0, y=0, width=1366, height=130)
#
#         # background image
#         bg1 = Image.open(r"Images_GUI\bg2.jpg")
#         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
#         self.photobg1 = ImageTk.PhotoImage(bg1)
#
#         # set image as label
#         bg_img = Label(self.root, image=self.photobg1)
#         bg_img.place(x=0, y=130, width=1366, height=768)
#
#         # title section
#         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"), bg="white",
#                           fg="navyblue")
#         title_lb1.place(x=0, y=0, width=1366, height=45)
#
#         # Create buttons below the section
#         # -------------------------------------------------------------------------------------------------------------------
#         # Training button 1
#         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
#         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
#         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
#
#         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
#         std_b1.place(x=600, y=170, width=180, height=180)
#
#         std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         std_b1_1.place(x=600, y=350, width=180, height=45)
#
#     # =====================Attendance===================
#
#     def mark_attendance(self, i, r, n):
#         now = datetime.now()
#         d1 = now.strftime("%d/%m/%Y")
#         dtString = now.strftime("%H:%M:%S")
#
#         cursor = self.conn.cursor()
#         cursor.execute(
#             "INSERT INTO attendance (Student_ID, Roll_No, Name, Date, Time, Status) VALUES (%s, %s, %s, %s, %s, %s)",
#             (i, r, n, d1, dtString, 'Present'))
#         self.conn.commit()
#
#     # ================face recognition==================
#     def face_recog(self):
#         def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
#             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
#
#             for (x, y, w, h) in features:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
#                 id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#
#                 confidence = int((100 * (1 - predict / 300)))
#
#                 if confidence > 77:
#                     cursor = self.conn.cursor()
#                     cursor.execute("SELECT Name, Roll_No, Student_ID FROM student WHERE Student_ID=" + str(id))
#                     result = cursor.fetchone()
#                     if result:
#                         n, r, i = result
#                     else:
#                         n, r, i = "Unknown", "Unknown", "Unknown"
#
#                     cv2.putText(img, f"Student ID: {i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
#                     cv2.putText(img, f"Name: {n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
#                     cv2.putText(img, f"Roll No: {r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 2)
#                     self.mark_attendance(i, r, n)
#
#                 else:
#                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
#
#         def recognize_faces(img, clf, faceCascade):
#             draw_boundray(img, faceCascade, 1.1, 10, (0, 255, 0), "Face", clf)
#             return img
#
#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("clf.xml")
#
#         videoCap = cv2.VideoCapture(0)
#
#         while True:
#             ret, img = videoCap.read()
#             img = recognize_faces(img, clf, faceCascade)
#             cv2.imshow("Face Detector", img)
#
#             if cv2.waitKey(1) == 13:
#                 break
#         videoCap.release()
#         cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     root = Tk()
#     conn = mysql.connector.connect(user='root', password='root123', host='localhost',
#                                    database='face_recognition', port=3306)
#     obj = Face_Recognition(root, conn)
#     root.mainloop()


# # from tkinter import *
# # from PIL import Image, ImageTk
# # import cv2
# # import mysql.connector
# # from datetime import datetime
# #
# # class Face_Recognition:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.geometry("1366x768+0+0")
# #         self.root.title("Face Recognition Panel")
# #
# #         # Header image
# #         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
# #         img = img.resize((1366, 130), Image.LANCZOS)
# #         self.photoimg = ImageTk.PhotoImage(img)
# #
# #         f_lb1 = Label(self.root, image=self.photoimg)
# #         f_lb1.place(x=0, y=0, width=1366, height=130)
# #
# #         # Background image
# #         bg1 = Image.open(r"Images_GUI\bg2.jpg")
# #         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
# #         self.photobg1 = ImageTk.PhotoImage(bg1)
# #
# #         bg_img = Label(self.root, image=self.photobg1)
# #         bg_img.place(x=0, y=130, width=1366, height=768)
# #
# #         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
# #                           bg="white", fg="navyblue")
# #         title_lb1.place(x=0, y=0, width=1366, height=45)
# #
# #         # Face Recognition button
# #         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
# #         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
# #         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
# #
# #         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
# #         std_b1.place(x=600, y=170, width=180, height=180)
# #
# #         std_b1_1 = Button(bg_img, command=self.take_attendance, text="Take Attendance", cursor="hand2",
# #                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
# #         std_b1_1.place(x=600, y=350, width=180, height=45)
# #
# #     def take_attendance(self):
# #         # Placeholder for attendance logic
# #         student_id = "123"
# #         roll_no = "001"
# #         name = "John Doe"
# #
# #         # Example: Writing attendance to a CSV file
# #         with open("attendance.csv", "a") as f:
# #             now = datetime.now()
# #             date_string = now.strftime("%d/%m/%Y")
# #             time_string = now.strftime("%H:%M:%S")
# #             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
# #
# #     def mark_attendance(self, i, r, n):
# #         with open("attendance.csv", "r+", newline="\n") as f:
# #             myDatalist = f.readlines()
# #             name_list = []
# #             for line in myDatalist:
# #                 entry = line.split(",")
# #                 name_list.append(entry[0])
# #
# #             if i not in name_list and r not in name_list and n not in name_list:
# #                 now = datetime.now()
# #                 d1 = now.strftime("%d/%m/%Y")
# #                 dtString = now.strftime("%H:%M:%S")
# #                 f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
# #
# #     def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
# #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
# #
# #         coord = []
# #
# #         for (x, y, w, h) in features:
# #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
# #
# #             confidence = int((100 * (1 - predict / 300)))
# #
# #             conn = mysql.connector.connect(username='root', password='root123', host='localhost',
# #                                             database='face_recognition', port=3306)
# #             cursor = conn.cursor()
# #
# #             cursor.execute("select Name from student where Student_ID=" + str(id))
# #             name_result = cursor.fetchone()
# #             if name_result:  # Check if result is not None
# #                 n = "+".join(name_result)
# #             else:
# #                 n = "Unknown"
# #
# #             cursor.execute("select Roll_No from student where Student_ID=" + str(id))
# #             roll_result = cursor.fetchone()
# #             if roll_result:  # Check if result is not None
# #                 r = "+".join(roll_result)
# #             else:
# #                 r = "Unknown"
# #
# #             cursor.execute("select Student_ID from student where Student_ID=" + str(id))
# #             id_result = cursor.fetchone()
# #             if id_result:  # Check if result is not None
# #                 i = "+".join(id_result)
# #             else:
# #                 i = "Unknown"
# #
# #             if isinstance(n, str):  # Check if n is a string
# #                 # No need to join if n is already a string
# #                 pass
# #             elif isinstance(n, (list, tuple)):  # Check if n is a list or tuple
# #                 # Join elements if n is a list or tuple
# #                 n = "+".join(n)
# #             else:
# #                 # Handle the case where n is neither a string nor an iterable
# #                 n = "Unknown"
# #
# #             if confidence > 77:
# #                 cv2.putText(img, f"Student_ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 self.mark_attendance(i, r, n)
# #             else:
# #                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
# #                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
# #
# #             coord = [x, y, w, y]
# #
# #         return coord
# #
# #     def face_recog(self):
# #         def recognize(img, clf, faceCascade):
# #             coord = self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
# #             return img
# #
# #         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# #         clf = cv2.face.LBPHFaceRecognizer_create()
# #         clf.read("clf.xml")
# #
# #         videoCap = cv2.VideoCapture(0)
# #
# #         while True:
# #             ret, img = videoCap.read()
# #             img = recognize(img, clf, faceCascade)
# #             cv2.imshow("Face Detector", img)
# #
# #             if cv2.waitKey(1) == 13:
# #                 break
# #
# #         videoCap.release()
# #         cv2.destroyAllWindows()
# #
# # if __name__ == "__main__":
# #     root = Tk()
# #     obj = Face_Recognition(root)
# #     root.mainloop()
#
# # # import re
# # from sys import path
# # from tkinter import *
# # from tkinter import ttk
# # from PIL import Image, ImageTk
# # import os
# # import mysql.connector
# # import cv2
# # import numpy as np
# # from tkinter import messagebox
# # from time import strftime
# # from datetime import datetime
# #
# #
# # class Face_Recognition:
# #
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.geometry("1366x768+0+0")
# #         self.root.title("Face Recognition Pannel")
# #
# #         # This part is image labels setting start
# #         # first header image
# #         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
# #         img = img.resize((1366, 130), Image.LANCZOS)
# #         self.photoimg = ImageTk.PhotoImage(img)
# #
# #         # set image as lable
# #         f_lb1 = Label(self.root, image=self.photoimg)
# #         f_lb1.place(x=0, y=0, width=1366, height=130)
# #
# #         # backgorund image
# #         bg1 = Image.open(r"Images_GUI\bg2.jpg")
# #         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
# #         self.photobg1 = ImageTk.PhotoImage(bg1)
# #
# #         # set image as lable
# #         bg_img = Label(self.root, image=self.photobg1)
# #         bg_img.place(x=0, y=130, width=1366, height=768)
# #
# #         # title section
# #         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Pannel", font=("verdana", 30, "bold"), bg="white",
# #                           fg="navyblue")
# #         title_lb1.place(x=0, y=0, width=1366, height=45)
# #
# #         # Create buttons below the section
# #         # -------------------------------------------------------------------------------------------------------------------
# #         # Training button 1
# #         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
# #         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
# #         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
# #
# #         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
# #         std_b1.place(x=600, y=170, width=180, height=180)
# #
# #         std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2",
# #                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
# #         std_b1_1.place(x=600, y=350, width=180, height=45)
# #
# #     # =====================Attendance===================
# #
# #     def mark_attendance(self, i, r, n):
# #         with open("attendance.csv", "r+", newline="\n") as f:
# #             myDatalist = f.readlines()
# #             name_list = []
# #             for line in myDatalist:
# #                 entry = line.split((","))
# #                 name_list.append(entry[0])
# #
# #             if ((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
# #                 now = datetime.now()
# #                 d1 = now.strftime("%d/%m/%Y")
# #                 dtString = now.strftime("%H:%M:%S")
# #                 f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
# #
# #     # ================face recognition==================
# #     def face_recog(self):
# #         def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
# #             gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #             featuers = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
# #
# #             coord = []
# #
# #             for (x, y, w, h) in featuers:
# #                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #                 id, predict = clf.predict(gray_image[y:y + h, x:x + w])
# #
# #                 confidence = int((100 * (1 - predict / 300)))
# #
# #                 conn = mysql.connector.connect(username='root', password='root123', host='localhost',
# #                                                database='face_recognition', port=3306)
# #                 cursor = conn.cursor()
# #
# #                 cursor.execute("select Name from student where Student_ID=" + str(id))
# #                 n = cursor.fetchone()
# #                 n = "+".join(n)
# #
# #                 cursor.execute("select Roll_No from student where Student_ID=" + str(id))
# #                 r = cursor.fetchone()
# #                 r = "+".join(r)
# #
# #                 cursor.execute("select Student_ID from student where Student_ID=" + str(id))
# #                 i = cursor.fetchone()
# #                 i = "+".join(i)
# #
# #                 if confidence > 77:
# #                     cv2.putText(img, f"Student_ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                     cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                     cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                     self.mark_attendance(i, r, n)
# #                 else:
# #                     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
# #                     cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
# #
# #                 coord = [x, y, w, y]
# #
# #             return coord
# #
# #             # ==========
# #
# #         def recognize(img, clf, faceCascade):
# #             coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
# #             return img
# #
# #         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# #         clf = cv2.face.LBPHFaceRecognizer_create()
# #         clf.read("clf.xml")
# #
# #         videoCap = cv2.VideoCapture(0)
# #
# #         while True:
# #             ret, img = videoCap.read()
# #             img = recognize(img, clf, faceCascade)
# #             cv2.imshow("Face Detector", img)
# #
# #             if cv2.waitKey(1) == 13:
# #                 break
# #         videoCap.release()
# #         cv2.destroyAllWindows()
# #
# #
# # if __name__ == "__main__":
# #     root = Tk()
# #     obj = Face_Recognition(root)
# #     root.mainloop()
#
# # from tkinter import *
# # from PIL import Image, ImageTk
# # import cv2
# # import mysql.connector
# # from datetime import datetime
# #
# # class Face_Recognition:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.geometry("1366x768+0+0")
# #         self.root.title("Face Recognition Panel")
# #
# #         # Header image
# #         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
# #         img = img.resize((1366, 130), Image.LANCZOS)
# #         self.photoimg = ImageTk.PhotoImage(img)
# #
# #         f_lb1 = Label(self.root, image=self.photoimg)
# #         f_lb1.place(x=0, y=0, width=1366, height=130)
# #
# #         # Background image
# #         bg1 = Image.open(r"Images_GUI\bg2.jpg")
# #         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
# #         self.photobg1 = ImageTk.PhotoImage(bg1)
# #
# #         bg_img = Label(self.root, image=self.photobg1)
# #         bg_img.place(x=0, y=130, width=1366, height=768)
# #
# #         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
# #                           bg="white", fg="navyblue")
# #         title_lb1.place(x=0, y=0, width=1366, height=45)
# #
# #         # Face Recognition button
# #         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
# #         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
# #         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
# #
# #         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
# #         std_b1.place(x=600, y=170, width=180, height=180)
# #
# #         std_b1_1 = Button(bg_img, command=self.take_attendance, text="Take Attendance", cursor="hand2",
# #                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
# #         std_b1_1.place(x=600, y=350, width=180, height=45)
# #
# #     def take_attendance(self):
# #         # Placeholder for attendance logic
# #         student_id = "123"
# #         roll_no = "001"
# #         name = "John Doe"
# #
# #         # Example: Writing attendance to a CSV file
# #         with open("attendance.csv", "a") as f:
# #             now = datetime.now()
# #             date_string = now.strftime("%d/%m/%Y")
# #             time_string = now.strftime("%H:%M:%S")
# #             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
# #
# #     def mark_attendance(self, i, r, n):
# #         with open("attendance.csv", "r+", newline="\n") as f:
# #             myDatalist = f.readlines()
# #             name_list = []
# #             for line in myDatalist:
# #                 entry = line.split(",")
# #                 name_list.append(entry[0])
# #
# #             if i not in name_list and r not in name_list and n not in name_list:
# #                 now = datetime.now()
# #                 d1 = now.strftime("%d/%m/%Y")
# #                 dtString = now.strftime("%H:%M:%S")
# #                 f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
# #
# #     def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
# #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
# #
# #         coord = []
# #
# #         for (x, y, w, h) in features:
# #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
# #
# #             confidence = int((100 * (1 - predict / 300)))
# #
# #             conn = mysql.connector.connect(username='root', password='root123', host='localhost',
# #                                             database='face_recognition', port=3306)
# #             cursor = conn.cursor()
# #
# #             cursor.execute("select Name from student where Student_ID=" + str(id))
# #             name_result = cursor.fetchone()
# #             if name_result:  # Check if result is not None
# #                 n = "+".join(name_result)
# #             else:
# #                 n = "Unknown"
# #
# #             cursor.execute("select Roll_No from student where Student_ID=" + str(id))
# #             roll_result = cursor.fetchone()
# #             if roll_result:  # Check if result is not None
# #                 r = "+".join(roll_result)
# #             else:
# #                 r = "Unknown"
# #
# #             cursor.execute("select Student_ID from student where Student_ID=" + str(id))
# #             id_result = cursor.fetchone()
# #             if id_result:  # Check if result is not None
# #                 i = "+".join(id_result)
# #             else:
# #                 i = "Unknown"
# #
# #             if isinstance(n, str):  # Check if n is a string
# #                 # No need to join if n is already a string
# #                 pass
# #             elif isinstance(n, (list, tuple)):  # Check if n is a list or tuple
# #                 # Join elements if n is a list or tuple
# #                 n = "+".join(n)
# #             else:
# #                 # Handle the case where n is neither a string nor an iterable
# #                 n = "Unknown"
# #
# #             if confidence > 77:
# #                 cv2.putText(img, f"Student_ID:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 self.mark_attendance(i, r, n)
# #             else:
# #                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
# #                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
# #
# #             coord = [x, y, w, y]
# #
# #         return coord
# #
# #     def face_recog(self):
# #         def recognize(img, clf, faceCascade):
# #             coord = self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
# #             return img
# #
# #         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# #         clf = cv2.face.LBPHFaceRecognizer_create()
# #         clf.read("clf.xml")
# #
# #         videoCap = cv2.VideoCapture(0)
# #
# #         while True:
# #             ret, img = videoCap.read()
# #             img = recognize(img, clf, faceCascade)
# #             cv2.imshow("Face Detector", img)
# #
# #             if cv2.waitKey(1) == 13:
# #                 break
# #
# #         videoCap.release()
# #         cv2.destroyAllWindows()
# #
# # if __name__ == "__main__":
# #     root = Tk()
# #     obj = Face_Recognition(root)
# #     root.mainloop()
#
#
# # from tkinter import *
# # from PIL import Image, ImageTk
# # import cv2
# # import mysql.connector
# # from datetime import datetime
# #
# # class Face_Recognition:
# #     def __init__(self, root):
# #         self.root = root
# #         self.root.geometry("1366x768+0+0")
# #         self.root.title("Face Recognition Panel")
# #
# #         # Header image
# #         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
# #         img = img.resize((1366, 130), Image.LANCZOS)
# #         self.photoimg = ImageTk.PhotoImage(img)
# #
# #         f_lb1 = Label(self.root, image=self.photoimg)
# #         f_lb1.place(x=0, y=0, width=1366, height=130)
# #
# #         # Background image
# #         bg1 = Image.open(r"Images_GUI\bg2.jpg")
# #         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
# #         self.photobg1 = ImageTk.PhotoImage(bg1)
# #
# #         bg_img = Label(self.root, image=self.photobg1)
# #         bg_img.place(x=0, y=130, width=1366, height=768)
# #
# #         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
# #                           bg="white", fg="navyblue")
# #         title_lb1.place(x=0, y=0, width=1366, height=45)
# #
# #         # Face Recognition button
# #         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
# #         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
# #         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
# #
# #         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
# #         std_b1.place(x=600, y=170, width=180, height=180)
# #
# #         std_b1_1 = Button(bg_img, command=self.take_attendance, text="Take Attendance", cursor="hand2",
# #                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
# #         std_b1_1.place(x=600, y=350, width=180, height=45)
# #
# #         # Database connection
# #         self.conn = mysql.connector.connect(username='root', password='root123', host='localhost',
# #                                             database='face_recognition', port=3306)
# #         self.cursor = self.conn.cursor()
# #
# #     def take_attendance(self):
# #         # Placeholder for attendance logic
# #         student_id = "1"
# #         roll_no = "22se02ml105"
# #         name = "ajay"
# #
# #         # Example: Writing attendance to a CSV file
# #         with open("attendance.csv", "a") as f:
# #             now = datetime.now()
# #             date_string = now.strftime("%d/%m/%Y")
# #             time_string = now.strftime("%H:%M:%S")
# #             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
# #
# #         # Inserting attendance into the database
# #         self.cursor.execute("INSERT INTO attendance (student_id, roll_no, name, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
# #                             (student_id, roll_no, name, date_string, time_string, "Present"))
# #         self.conn.commit()
# #
# #     def mark_attendance(self, i, r, n):
# #         with open("attendance.csv", "r+", newline="\n") as f:
# #             myDatalist = f.readlines()
# #             name_list = []
# #             for line in myDatalist:
# #                 entry = line.split(",")
# #                 name_list.append(entry[0])
# #
# #             if i not in name_list and r not in name_list and n not in name_list:
# #                 now = datetime.now()
# #                 d1 = now.strftime("%d/%m/%Y")
# #                 dtString = now.strftime("%H:%M:%S")
# #                 f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
# #
# #     def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
# #         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
# #
# #         coord = []
# #
# #         for (x, y, w, h) in features:
# #             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
# #
# #             confidence = int((100 * (1 - predict / 300)))
# #
# #             self.cursor.execute("select name, roll_no from student where student_id = %s", (id,))
# #             name_result = self.cursor.fetchone()
# #             if name_result:  # Check if result is not None
# #                 n, r = name_result
# #             else:
# #                 n, r = "Unknown", "Unknown"
# #
# #             if confidence > 60:  # Adjust confidence threshold as needed
# #                 cv2.putText(img, f"Student_ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
# #                 self.mark_attendance(id, r, n)
# #             else:
# #                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
# #                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
# #
# #             coord = [x, y, w, y]
# #
# #         return coord
# #
# #     def face_recog(self):
# #         def recognize(img, clf, faceCascade):
# #             coord = self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
# #             return img
# #
# #         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# #         clf = cv2.face.LBPHFaceRecognizer_create()
# #         clf.read("clf.xml")
# #
# #         videoCap = cv2.VideoCapture(0)
# #
# #         while True:
# #             ret, img = videoCap.read()
# #             img = recognize(img, clf, faceCascade)
# #             cv2.imshow("Face Detector", img)
# #
# #             key = cv2.waitKey(1)
# #             if key == 13:  # Break the loop when Enter key is pressed
# #                 break
# #             elif key == ord('p') or key == ord('P'):  # Press 'P' key to take attendance
# #                 self.take_attendance()  # Call the take attendance method
# #
# #         videoCap.release()
# #         cv2.destroyAllWindows()
# #
# # if __name__ == "__main__":
# #     root = Tk()
# #     obj = Face_Recognition(root)
# #     root.mainloop()
#
# from tkinter import *
# from PIL import Image, ImageTk
# import cv2
# import mysql.connector
# from datetime import datetime
#
#
# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition Panel")
#
#         # Header image
#         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
#         img = img.resize((1366, 130), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)
#
#         f_lb1 = Label(self.root, image=self.photoimg)
#         f_lb1.place(x=0, y=0, width=1366, height=130)
#
#         # Background image
#         bg1 = Image.open(r"Images_GUI\bg2.jpg")
#         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
#         self.photobg1 = ImageTk.PhotoImage(bg1)
#
#         bg_img = Label(self.root, image=self.photobg1)
#         bg_img.place(x=0, y=130, width=1366, height=768)
#
#         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
#                           bg="white", fg="navyblue")
#         title_lb1.place(x=0, y=0, width=1366, height=45)
#
#         # Face Recognition button
#         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
#         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
#         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
#
#         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
#         std_b1.place(x=600, y=170, width=180, height=180)
#
#         std_b1_1 = Button(bg_img, command=self.take_attendance, text="Take Attendance", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         std_b1_1.place(x=600, y=350, width=180, height=45)
#
#         # Database connection
#         self.conn = mysql.connector.connect(username='root', password='root123', host='localhost',
#                                             database='face_recognition', port=3306)
#         self.cursor = self.conn.cursor()
#
#     def take_attendance(self):
#         # Placeholder for attendance logic
#         student_id = "1"
#         roll_no = "22se02ml105"
#         name = "ajay"
#
#         # Example: Writing attendance to a CSV file
#         with open("attendance.csv", "a") as f:
#             now = datetime.now()
#             date_string = now.strftime("%d/%m/%Y")
#             time_string = now.strftime("%H:%M:%S")
#             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
#
#         # Inserting attendance into the database
#         self.cursor.execute(
#             "INSERT INTO attendance (student_id, roll_no, name, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
#             (student_id, roll_no, name, date_string, time_string, "Present"))
#         self.conn.commit()
#
#         return date_string, time_string  # returning date and time strings
#
#     def mark_attendance(self, student_id, roll_no, name, date_string, time_string):
#         with open("attendance.csv", "a") as f:
#             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
#
#         self.cursor.execute(
#             "INSERT INTO attendance (student_id, roll_no, name, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
#             (student_id, roll_no, name, date_string, time_string, "Present"))
#         self.conn.commit()
#
#     def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf, date_string, time_string):
#         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
#
#         coord = []
#
#         for (x, y, w, h) in features:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#
#             confidence = int((100 * (1 - predict / 300)))
#
#             self.cursor.execute("select name, roll_no from student where student_id = %s", (id,))
#             name_result = self.cursor.fetchone()
#             if name_result:  # Check if result is not None
#                 n, r = name_result
#             else:
#                 n, r = "Unknown", "Unknown"
#
#             if confidence > 60:  # Adjust confidence threshold as needed
#                 cv2.putText(img, f"Student_ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                 cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                 cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                 self.mark_attendance(id, r, n, date_string, time_string)
#             else:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
#
#             coord = [x, y, w, y]
#
#         return coord
#
#     def face_recog(self):
#         def recognize(img, clf, faceCascade, date_string, time_string):  # pass date and time strings
#             coord = self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf, date_string, time_string)
#             return img
#
#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("clf.xml")
#
#         videoCap = cv2.VideoCapture(0)
#
#         while True:
#             ret, img = videoCap.read()
#             date_string, time_string = self.take_attendance()  # call take_attendance to get date and time
#             img = recognize(img, clf, faceCascade, date_string, time_string)  # pass date and time strings
#             cv2.imshow("Face Detector", img)
#
#             key = cv2.waitKey(1)
#             if key == 13:  # Break the loop when Enter key is pressed
#                 break
#             elif key == ord('p') or key == ord('P'):  # Press 'P' key to take attendance
#                 self.take_attendance()  # Call the take attendance method
#
#         videoCap.release()
#         cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# import cv2
# import numpy as np
# import mysql.connector
# from datetime import datetime
#
#
# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition Panel")
#
#         # Header image
#         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")  # Update with your image path
#         img = img.resize((1366, 130), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)
#
#         f_lb1 = Label(self.root, image=self.photoimg)
#         f_lb1.place(x=0, y=0, width=1366, height=130)
#
#         # Background image
#         bg1 = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\bg2.jpg")  # Update with your image path
#         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
#         self.photobg1 = ImageTk.PhotoImage(bg1)
#
#         bg_img = Label(self.root, image=self.photobg1)
#         bg_img.place(x=0, y=130, width=1366, height=768)
#
#         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
#                           bg="white", fg="navyblue")
#         title_lb1.place(x=0, y=0, width=1366, height=45)
#
#         # Face Recognition button
#         std_img_btn = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\f_det.jpg")  # Update with your image path
#         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
#         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
#
#         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
#         std_b1.place(x=600, y=170, width=180, height=180)
#
#         std_b1_1 = Button(bg_img, text="Close", command=self.close, cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         std_b1_1.place(x=600, y=350, width=180, height=45)
#
#         # Database connection
#         self.conn = mysql.connector.connect(username='root', password='root123', host='localhost',
#                                             database='face_recognition', port=3306)
#         self.cursor = self.conn.cursor()
#
#     def mark_attendance(self, student_id, roll_no, name, date_string, time_string):
#         with open("attendance.csv", "a") as f:
#             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
#
#         self.cursor.execute(
#             "INSERT INTO attendance (student_id, roll_no, name, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
#             (student_id, roll_no, name, date_string, time_string, "Present"))
#         self.conn.commit()
#
#     def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
#         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
#
#         for (x, y, w, h) in features:
#             cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
#             roi_gray = gray_image[y:y + h, x:x + w]
#
#             # Recognize face
#             id_, confidence = clf.predict(roi_gray)
#             if confidence >= 45 and confidence <= 85:  # Adjust confidence threshold as needed
#                 self.cursor.execute("SELECT name, roll_no FROM student WHERE id = %s", (id_,))
#                 result = self.cursor.fetchone()
#                 if result:
#                     name, roll_no = result
#                     cv2.putText(img, f"Name: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#                     cv2.putText(img, f"Roll No: {roll_no}", (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#                     now = datetime.now()
#                     date_string = now.strftime("%d/%m/%Y")
#                     time_string = now.strftime("%H:%M:%S")
#                     self.mark_attendance(id_, roll_no, name, date_string, time_string)
#             else:
#                 cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
#
#     def face_recog(self):
#         face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # Update with your cascade path
#         recognizer = cv2.face.LBPHFaceRecognizer_create()
#         recognizer.read("C:/Users/ajays/PycharmProjects/facial recognition attendance system/clf.xml")  # Update with your trained model path
#
#         cap = cv2.VideoCapture(0)
#
#         while True:
#             ret, frame = cap.read()
#             self.draw_boundary(frame, face_cascade, 1.1, 5, (255, 0, 0), "Face", recognizer)
#             cv2.imshow('Face Recognition', frame)
#
#             if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
#                 break
#
#         cap.release()
#         cv2.destroyAllWindows()
#
#     def close(self):
#         self.root.destroy()
#
#
# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()

# from tkinter import *
# from PIL import Image, ImageTk
# import cv2
# import mysql.connector
# from datetime import datetime
#
#
# class Face_Recognition:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face Recognition Panel")
#
#         # Header image
#         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
#         img = img.resize((1366, 130), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)
#
#         f_lb1 = Label(self.root, image=self.photoimg)
#         f_lb1.place(x=0, y=0, width=1366, height=130)
#
#         # Background image
#         bg1 = Image.open(r"Images_GUI\bg2.jpg")
#         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
#         self.photobg1 = ImageTk.PhotoImage(bg1)
#
#         bg_img = Label(self.root, image=self.photobg1)
#         bg_img.place(x=0, y=130, width=1366, height=768)
#
#         title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
#                           bg="white", fg="navyblue")
#         title_lb1.place(x=0, y=0, width=1366, height=45)
#
#         # Face Recognition button
#         std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
#         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
#         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
#
#         std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
#         std_b1.place(x=600, y=170, width=180, height=180)
#
#         std_b1_1 = Button(bg_img, text="Close", command=self.close, cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         std_b1_1.place(x=600, y=350, width=180, height=45)
#
#         # Database connection
#         self.conn = mysql.connector.connect(username='root', password='root123', host='localhost',
#                                             database='face_recognition', port=3306)
#         self.cursor = self.conn.cursor()
#
#     def mark_attendance(self, student_id, roll_no, name, date_string, time_string):
#         with open("attendance.csv", "a") as f:
#             f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
#
#         self.cursor.execute(
#             "INSERT INTO attendance (student_id, roll_no, name, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
#             (student_id, roll_no, name, date_string, time_string, "Present"))
#         self.conn.commit()
#
#     def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf, date_string, time_string):
#         gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
#
#         for (x, y, w, h) in features:
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
#             id, predict = clf.predict(gray_image[y:y + h, x:x + w])
#
#             confidence = int((100 * (1 - predict / 300)))
#
#             self.cursor.execute("select name, roll_no from student where student_id = %s", (id,))
#             name_result = self.cursor.fetchone()
#             if name_result:  # Check if result is not None
#                 n, r = name_result
#             else:
#                 n, r = "Unknown", "Unknown"
#
#             if confidence > 60:  # Adjust confidence threshold as needed
#                 cv2.putText(img, f"Student_ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                 cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                 cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
#                 now = datetime.now()
#                 date_string = now.strftime("%d/%m/%Y")
#                 time_string = now.strftime("%H:%M:%S")
#                 self.mark_attendance(id, r, n, date_string, time_string)
#             else:
#                 cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
#                 cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)
#
#     def face_recog(self):
#         faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.read("clf.xml")
#
#         videoCap = cv2.VideoCapture(0)
#
#         while True:
#             ret, img = videoCap.read()
#             self.draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf, "", "")
#             cv2.imshow("Face Detector", img)
#
#             key = cv2.waitKey(1)
#             if key == 13:  # Break the loop when Enter key is pressed
#                 break
#             elif key == ord('p') or key == ord('P'):  # Press 'P' key to take attendance
#                 pass  # Attendance is marked during face detection
#
#         videoCap.release()
#         cv2.destroyAllWindows()
#
#     def close(self):
#         self.root.destroy()
#
#
# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition(root)
#     root.mainloop()


import os
from tkinter import *
from tkinter import messagebox  # Import messagebox
from PIL import Image, ImageTk
import cv2
import mysql.connector
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")

        # Header image
        img = Image.open("Images_GUI/banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open("Images_GUI/bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=("verdana", 30, "bold"),
                          bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Face Recognition button
        std_img_btn = Image.open("Images_GUI/f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.face_recog, image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)

        std_b1_1 = Button(bg_img, text="Take Attendance", command=self.take_attendance, cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

        # Database connection
        try:
            self.conn = mysql.connector.connect(user='root', password='root123', host='localhost',
                                                database='face_recognition', port=3306)
            self.cursor = self.conn.cursor()
            print("Database connection successful.")
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")

        # Load classifier
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.clf = cv2.face.LBPHFaceRecognizer_create()
        self.clf.read("clf.xml")

        # Set to track recognized students
        self.recognized_students = {}

    def mark_attendance(self, student_id, roll_no, name, date_string, time_string):
        # Log the attendance into the CSV file
        with open("attendance.csv", "a") as f:
            f.write(f"{student_id},{roll_no},{name},{date_string},{time_string},Present\n")
        print(f"Logged attendance for {name} ({roll_no})")

        # Insert attendance into the database
        try:
            print(f"Inserting to database: {student_id}, {roll_no}, {name}, {date_string}, {time_string}, Present")
            self.cursor.execute(
                "INSERT INTO attendance (student_id, roll_no, name, date, time, status) VALUES (%s, %s, %s, %s, %s, %s)",
                (student_id, roll_no, name, date_string, time_string, "Present"))
            self.conn.commit()
            print(f"Saved to database: {student_id}, {roll_no}, {name}, {date_string}, {time_string}, Present")

            # Show success message
            messagebox.showinfo("Success", f"Attendance marked for {name} (Roll No: {roll_no})")
        except mysql.connector.Error as e:
            print(f"Error saving to database: {e}")
            messagebox.showerror("Error", f"Could not mark attendance for {name}.")

    def recognize_face(self, img):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = self.faceCascade.detectMultiScale(gray_image, 1.1, 10)

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
            id, predict = self.clf.predict(gray_image[y:y + h, x:x + w])

            confidence = int((100 * (1 - predict / 300)))

            if confidence > 60:  # Adjust confidence threshold as needed
                self.cursor.execute("SELECT name, roll_no FROM student WHERE student_id = %s", (id,))
                name_result = self.cursor.fetchone()
                if name_result:
                    n, r = name_result
                else:
                    n, r = "Unknown", "Unknown"

                # Store recognized students with details for attendance marking
                if id not in self.recognized_students:
                    self.recognized_students[id] = (r, n)  # Store roll_no and name
                    print(f"Recognized: {n} (Roll No: {r}, ID: {id})")

                # Display recognized student information
                cv2.putText(img, f"Student_ID:{id}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                cv2.putText(img, f"Roll-No:{r}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
            else:
                # If confidence is low, it is treated as an unknown face
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

        return img  # Return the processed image

    def face_recog(self):
        self.recognized_students.clear()  # Clear the set for a new session
        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = self.recognize_face(img)
            cv2.imshow("Face Detector", img)

            if cv2.waitKey(1) == 13:  # Break the loop when Enter key is pressed
                break

        videoCap.release()
        cv2.destroyAllWindows()

    def take_attendance(self):
        videoCap = cv2.VideoCapture(0)

        while True:
            ret, img = videoCap.read()
            img = self.recognize_face(img)
            cv2.imshow("Face Detector", img)

            key = cv2.waitKey(1)
            if key == 13:  # Break the loop when Enter key is pressed
                # Mark attendance for recognized students
                now = datetime.now()
                date_string = now.strftime("%d/%m/%Y")
                time_string = now.strftime("%H:%M:%S")

                if self.recognized_students:  # Check if there are any recognized students
                    for student_id, (roll_no, name) in self.recognized_students.items():
                        self.mark_attendance(student_id, roll_no, name, date_string, time_string)
                else:
                    messagebox.showwarning("No Students Recognized", "No students were recognized for attendance.")

                self.recognized_students.clear()  # Clear recognized students after marking
                break

        videoCap.release()
        cv2.destroyAllWindows()

    def close(self):
        self.conn.close()  # Close the database connection when closing the app
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

