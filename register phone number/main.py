import os
import tkinter as tk
from tkinter import messagebox


def create_phone_number_file():
    num_students = entry_num_students.get()

    if num_students.isdigit() and int(num_students) > 0:
        num_students = int(num_students)
        student_info = [(entry_student_names[i].get(), entry_phone_numbers[i].get())
                        for i in range(num_students)
                        if entry_student_names[i].get() and entry_phone_numbers[i].get()]

        if student_info:
            phone_number_directory = "D:\\Face Recognition-Based Attendance System\\register phone number\\register numbers"
            phone_number_file_path = os.path.join(phone_number_directory, "phone_numbers.txt")

            with open(phone_number_file_path, "w") as file:
                for name, phone_number in student_info:
                    file.write(f"{name}, {phone_number}\n")

            messagebox.showinfo("Success", "Phone number file created.")
        else:
            messagebox.showwarning("No Information", "Please enter student names and phone numbers.")
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number of students.")


# Create the main window
root = tk.Tk()
root.title("Create Phone Number File")

# Label and Entry for number of students
label_num_students = tk.Label(root, text="Number of Students:")
label_num_students.pack()
entry_num_students = tk.Entry(root)
entry_num_students.pack()

# Label and Entry for student names and phone numbers
label_student_info = tk.Label(root, text="Student Information:")
label_student_info.pack()

entry_student_names = []
entry_phone_numbers = []
for _ in range(5):  # Adjust the range according to your needs
    entry_student = tk.Entry(root)
    entry_student.pack()
    entry_student_names.append(entry_student)

    entry_phone = tk.Entry(root)
    entry_phone.pack()
    entry_phone_numbers.append(entry_phone)

# Button to create the phone number file
button_create_file = tk.Button(root, text="Create Phone Number File", command=create_phone_number_file)
button_create_file.pack()

# Start the main loop
root.mainloop()