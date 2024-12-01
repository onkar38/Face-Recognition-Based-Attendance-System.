import cv2
import os
import tkinter as tk
from tkinter import messagebox


def register_face(name):
    # Create a directory for storing face images if it doesn't exist
    if not os.path.exists('faces'):
        os.makedirs('faces')

    # Initialize the webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the webcam
        ret, frame = video_capture.read()

        # Display the frame
        cv2.imshow('Video', frame)

        # Check for user input to save the image
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Save the image with the student's name
            image_path = os.path.join('faces', f'{name}.jpg')
            cv2.imwrite(image_path, frame)
            messagebox.showinfo("Success", f"Face image saved as {name}.jpg")
            break

    # Release the webcam and close the window
    video_capture.release()
    cv2.destroyAllWindows()


def register_faces():
    num_students = entry_num_students.get()

    if num_students.isdigit() and int(num_students) > 0:
        num_students = int(num_students)
        student_names = [entry_student_names[i].get() for i in range(num_students) if entry_student_names[i].get()]

        if student_names:
            for name in student_names:
                register_face(name)
        else:
            messagebox.showwarning("No Names", "Please enter student names.")
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number of students.")


def create_faces_window():
    global entry_num_students, entry_student_names

    # Create a new window
    faces_window = tk.Toplevel(root)
    faces_window.title("Register Faces")

    # Label and Entry for number of students
    label_num_students = tk.Label(faces_window, text="Number of Students:")
    label_num_students.pack()
    entry_num_students = tk.Entry(faces_window)
    entry_num_students.pack()

    # Button to register faces
    button_register_faces = tk.Button(faces_window, text="Register Faces", command=register_faces)
    button_register_faces.pack()

    # Label and Entry for student names
    label_student_names = tk.Label(faces_window, text="Student Names:")
    label_student_names.pack()

    entry_student_names = []
    for _ in range(5):  # Adjust the range according to your needs
        entry_student = tk.Entry(faces_window)
        entry_student.pack()
        entry_student_names.append(entry_student)


# Create the main window
root = tk.Tk()
root.title("Face Registration")

# Button to open faces window
button_open_faces = tk.Button(root, text="Open Faces Window", command=create_faces_window)
button_open_faces.pack()

# Start the main loop
root.mainloop()