from tkinter import *
from tkinter import messagebox
import subprocess


def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'onkar' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
        clear_window()
        new_page()
    else:
        messagebox.showerror('Error', 'Login Failed')


# Subprocess calls for each button
def register_faces():
    subprocess.call(['python', 'D:\\Face Recognition-Based Attendance System\\register faces\\main.py'])


def register_phone_numbers():
    subprocess.call(['python', 'D:\\Face Recognition-Based Attendance System\\register phone number\\main.py'])


def start_attendance():
    subprocess.call(['python', 'D:\\Face Recognition-Based Attendance System\\attendance\\main.py'])


def see_attendance():
    subprocess.call(['python', 'D:\\Face Recognition-Based Attendance System\\attendance files'])


def clear_window():
    # Destroy all widgets in the window
    for widget in root.winfo_children():
        widget.destroy()


def new_page():
    root.configure(background='#0096DC')

    # Frame for buttons to organize layout
    button_frame = Frame(root, bg='#0096DC')
    button_frame.pack(expand=True)

    # Buttons arranged in the frame with proper spacing
    register_faces_btn = Button(button_frame, text='Register Faces', width=20, height=2, command=register_faces)
    register_faces_btn.grid(row=0, column=0, pady=20, padx=50)

    register_numbers_btn = Button(button_frame, text='Register Phone Numbers', width=20, height=2,
                                  command=register_phone_numbers)
    register_numbers_btn.grid(row=1, column=0, pady=20, padx=50)

    attendance_btn = Button(button_frame, text='Start Attendance', width=20, height=2, command=start_attendance)
    attendance_btn.grid(row=2, column=0, pady=20, padx=50)

    see_attendance_btn = Button(button_frame, text='See Attendance', width=20, height=2, command=see_attendance)
    see_attendance_btn.grid(row=3, column=0, pady=20, padx=50)


# Main login window
root = Tk()

root.title('Login Form')
root.geometry('550x700')  # Reduced height for a compact layout
root.configure(background='#0096DC')

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(50, 5))
email_label.config(font=('verdana', 22))

email_input = Entry(root, width=40)
email_input.pack(ipady=6, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(10, 8))
password_label.config(font=('verdana', 22))

password_input = Entry(root, width=40, show='*')
password_input.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, command=handle_login)
login_btn.pack(pady=(40, 50))
login_btn.config(font=('verdana', 10))

root.mainloop()
