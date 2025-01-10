# from tkinter import *
# from tkinter import ttk
# from train import Train
# from PIL import Image, ImageTk
# from student import Student
# from train import Train
# from face_recognition import Face_Recognition
# from attendance import Attendance
# from developer import Developer
# import os
# from helpsupport import Helpsupport
#
#
# class Face_Recognition_System:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1366x768+0+0")
#         self.root.title("Face_Recogonition_System")
#
#         # This part is image labels setting start
#         # first header image
#         img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
#         img = img.resize((1366, 130), Image.LANCZOS)
#         self.photoimg = ImageTk.PhotoImage(img)
#
#         # set image as lable
#         f_lb1 = Label(self.root, image=self.photoimg)
#         f_lb1.place(x=0, y=0, width=1366, height=130)
#
#         # backgorund image
#         bg1 = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\bg3.jpg")
#         bg1 = bg1.resize((1366, 768), Image.LANCZOS)
#         self.photobg1 = ImageTk.PhotoImage(bg1)
#
#         # set image as lable
#         bg_img = Label(self.root, image=self.photobg1)
#         bg_img.place(x=0, y=130, width=1366, height=768)
#
#         # title section
#         title_lb1 = Label(bg_img, text="Attendance Managment System Using Facial Recognition",
#                           font=("verdana", 30, "bold"), bg="white", fg="navyblue")
#         title_lb1.place(x=0, y=0, width=1366, height=45)
#
#         # Create buttons below the section
#         # -------------------------------------------------------------------------------------------------------------------
#         # student button 1
#         std_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\std1.jpg")
#         std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
#         self.std_img1 = ImageTk.PhotoImage(std_img_btn)
#
#         std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
#         std_b1.place(x=250, y=100, width=180, height=180)
#
#         std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student Pannel", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         std_b1_1.place(x=250, y=280, width=180, height=45)
#
#         # Detect Face  button 2
#         det_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\det1.jpg")
#         det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)
#         self.det_img1 = ImageTk.PhotoImage(det_img_btn)
#
#         det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2", )
#         det_b1.place(x=480, y=100, width=180, height=180)
#
#         det_b1_1 = Button(bg_img, command=self.face_rec, text="Face Detector", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         det_b1_1.place(x=480, y=280, width=180, height=45)
#
#         # Attendance System  button 3
#         att_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\att.jpg")
#         att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
#         self.att_img1 = ImageTk.PhotoImage(att_img_btn)
#
#         att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2", )
#         att_b1.place(x=710, y=100, width=180, height=180)
#
#         att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Attendance", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         att_b1_1.place(x=710, y=280, width=180, height=45)
#
#         # Help  Support  button 4
#         hlp_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\hlp.jpg")
#         hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)
#         self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)
#
#         hlp_b1 = Button(bg_img, command=self.helpSupport, image=self.hlp_img1, cursor="hand2", )
#         hlp_b1.place(x=940, y=100, width=180, height=180)
#
#         hlp_b1_1 = Button(bg_img, command=self.helpSupport, text="Help Support", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         hlp_b1_1.place(x=940, y=280, width=180, height=45)
#
#         # Top 4 buttons end.......
#         # ---------------------------------------------------------------------------------------------------------------------------
#         # Start below buttons.........
#         # Train   button 5
#         tra_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\tra1.jpg")
#         tra_img_btn = tra_img_btn.resize((180, 180), Image.LANCZOS)
#         self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)
#
#         tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2", )
#         tra_b1.place(x=250, y=330, width=180, height=180)
#
#         tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Data Train", cursor="hand2",
#                           font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
#         tra_b1_1.place(x=250, y=510, width=180, height=45)
#
#         # Photo   button 6
#         pho_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\qr1.png")
#         pho_img_btn = pho_img_btn.resize((180, 180), Image.LANCZOS)
#         self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)
#
#         pho_b1 = Button(bg_img, command=self.open_img, image=self.pho_img1, cursor="hand2", )
#         pho_b1.place(x=480, y=330, width=180, height=180)
#
#         pho_b1_1 = Button(bg_img, command=self.open_img, text="QR-Codes", cursor="hand2", font=("tahoma", 15, "bold"),
#                           bg="white", fg="navyblue")
#         pho_b1_1.place(x=480, y=510, width=180, height=45)
#
#         # Developers   button 7
#         dev_img_btn = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\dev.jpg")
#         dev_img_btn = dev_img_btn.resize((180, 180), Image.LANCZOS)
#         self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)
#
#         dev_b1 = Button(bg_img, command=self.developr, image=self.dev_img1, cursor="hand2", )
#         dev_b1.place(x=710, y=330, width=180, height=180)
#
#         dev_b1_1 = Button(bg_img, command=self.developr, text="Developers", cursor="hand2", font=("tahoma", 15, "bold"),
#                           bg="white", fg="navyblue")
#         dev_b1_1.place(x=710, y=510, width=180, height=45)
#
#         # exit   button 8
#         exi_img_btn = Image.open(
#             r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\exi.jpg")
#         exi_img_btn = exi_img_btn.resize((180, 180), Image.LANCZOS)
#         self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)
#
#         exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2", )
#         exi_b1.place(x=940, y=330, width=180, height=180)
#
#         exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"),
#                           bg="white", fg="navyblue")
#         exi_b1_1.place(x=940, y=510, width=180, height=45)
#
#     # ==================Funtion for Open Images Folder==================
#     def open_img(self):
#         os.startfile("dataset")
#
#     # ==================Functions Buttons=====================
#     def student_pannels(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Student(self.new_window)
#
#     def train_pannels(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Train(self.new_window)
#
#     def face_rec(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Face_Recognition(self.new_window)
#
#     def attendance_pannel(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Attendance(self.new_window)
#
#     def developr(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Developer(self.new_window)
#
#     def helpSupport(self):
#         self.new_window = Toplevel(self.root)
#         self.app = Helpsupport(self.new_window)
#
#     def Close(self):
#         root.destroy()
#
#
# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition_System(root)
#     root.mainloop()


from tkinter import *
from tkinter import ttk, scrolledtext
from train import Train
from PIL import Image, ImageTk
from student import Student
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport
from chatbot import Chatbot  # Import the chatbot class
from googlesearch import search  # For Google search functionality in chatbot


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recognition_System")

        # This part is image labels setting start
        # first header image
        img = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        # set image as label
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # background image
        bg1 = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # title section
        title_lb1 = Label(bg_img, text="Attendance Management System Using Facial Recognition",
                          font=("verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Create buttons below the section
        # -------------------------------------------------------------------------------------------------------------------
        # student button 1
        std_img_btn = Image.open(
            r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\std1.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img, command=self.student_pannels, image=self.std_img1, cursor="hand2")
        std_b1.place(x=250, y=100, width=180, height=180)

        std_b1_1 = Button(bg_img, command=self.student_pannels, text="Student Panel", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=250, y=280, width=180, height=45)

        # Detect Face button 2
        det_img_btn = Image.open(
            r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\det1.jpg")
        det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)
        self.det_img1 = ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img, command=self.face_rec, image=self.det_img1, cursor="hand2")
        det_b1.place(x=480, y=100, width=180, height=180)

        det_b1_1 = Button(bg_img, command=self.face_rec, text="Face Detector", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        det_b1_1.place(x=480, y=280, width=180, height=45)

        # Attendance System button 3
        att_img_btn = Image.open(
            r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\att.jpg")
        att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
        self.att_img1 = ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img, command=self.attendance_pannel, image=self.att_img1, cursor="hand2")
        att_b1.place(x=710, y=100, width=180, height=180)

        att_b1_1 = Button(bg_img, command=self.attendance_pannel, text="Attendance", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        att_b1_1.place(x=710, y=280, width=180, height=45)

        # Help Support button 4
        hlp_img_btn = Image.open(
            r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\hlp.jpg")
        hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)
        self.hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img, command=self.helpSupport, image=self.hlp_img1, cursor="hand2")
        hlp_b1.place(x=940, y=100, width=180, height=180)

        hlp_b1_1 = Button(bg_img, command=self.helpSupport, text="Help Support", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        hlp_b1_1.place(x=940, y=280, width=180, height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
        # Train button 5
        tra_img_btn = Image.open(
            r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\tra1.jpg")
        tra_img_btn = tra_img_btn.resize((180, 180), Image.LANCZOS)
        self.tra_img1 = ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img, command=self.train_pannels, image=self.tra_img1, cursor="hand2")
        tra_b1.place(x=250, y=330, width=180, height=180)

        tra_b1_1 = Button(bg_img, command=self.train_pannels, text="Data Train", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        tra_b1_1.place(x=250, y=510, width=180, height=45)

        # Chatbot button 6 (Replacing QR Code)
        pho_img_btn = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\qr1.png")
        pho_img_btn = pho_img_btn.resize((180, 180), Image.LANCZOS)
        self.pho_img1 = ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img, command=self.chatbot_pannel, image=self.pho_img1, cursor="hand2")
        pho_b1.place(x=480, y=330, width=180, height=180)

        pho_b1_1 = Button(bg_img, command=self.chatbot_pannel, text="Chatbot", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        pho_b1_1.place(x=480, y=510, width=180, height=45)

        # Developers button 7
        dev_img_btn = Image.open(r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\dev.jpg")
        dev_img_btn = dev_img_btn.resize((180, 180), Image.LANCZOS)
        self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img, command=self.developr, image=self.dev_img1, cursor="hand2")
        dev_b1.place(x=710, y=330, width=180, height=180)

        dev_b1_1 = Button(bg_img, command=self.developr, text="Developers", cursor="hand2",
                          font=("tahoma", 15, "bold"), bg="white", fg="navyblue")
        dev_b1_1.place(x=710, y=510, width=180, height=45)

        # Exit button 8
        exi_img_btn = Image.open(
            r"C:\Users\ajays\PycharmProjects\facial recognition attendance system\Images_GUI\exi.jpg")
        exi_img_btn = exi_img_btn.resize((180, 180), Image.LANCZOS)
        self.exi_img1 = ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img, command=self.Close, image=self.exi_img1, cursor="hand2")
        exi_b1.place(x=940, y=330, width=180, height=180)

        exi_b1_1 = Button(bg_img, command=self.Close, text="Exit", cursor="hand2", font=("tahoma", 15, "bold"),
                          bg="white", fg="navyblue")
        exi_b1_1.place(x=940, y=510, width=180, height=45)

    # Functions for the buttons
    def student_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_pannels(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_rec(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_pannel(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developr(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helpSupport(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)

    def Close(self):
        root.destroy()

    # Add the chatbot window opening method
    def chatbot_pannel(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Chatbot Interface")
        self.new_window.geometry("600x400")

        # Load background image
        bg_image = Image.open(r"C:\Users\ajays\PycharmProjects\chatbot\chatbotimage.jpg")
        bg_image = bg_image.resize((600, 400), Image.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a label for the background image
        bg_label = Label(self.new_window, image=bg_photo)
        bg_label.image = bg_photo  # To avoid garbage collection of the image
        bg_label.place(x=0, y=0)

        # Create a scrolled text area for chat history
        chat_history = scrolledtext.ScrolledText(self.new_window, wrap=WORD, state=DISABLED, bg='white')
        chat_history.place(x=20, y=20, width=560, height=300)

        # Entry widget for user input
        user_input_entry = Entry(self.new_window, width=50)
        user_input_entry.place(x=20, y=340)

        # Send button
        send_button = Button(self.new_window, text="Send", command=lambda: self.send_message(chat_history, user_input_entry))
        send_button.place(x=500, y=337)

        self.chatbot = Chatbot("chat_bot.csv")  # Initialize the chatbot

    # Add send_message method to handle sending messages in chatbot
    def send_message(self, chat_history, user_input_entry):
        user_input = user_input_entry.get()
        if not user_input.strip():
            return

        chat_history.config(state=NORMAL)
        chat_history.insert(END, f"You: {user_input}\n")

        response = chatbot_response(self.chatbot, user_input)
        chat_history.insert(END, f"Bot: {response}\n\n")

        chat_history.config(state=DISABLED)
        chat_history.yview(END)  # Scroll to the end
        user_input_entry.delete(0, END)  # Clear input field


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
