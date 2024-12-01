import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime
import os

video_capture = cv2.VideoCapture(0)

# Path to the folder containing face images
faces_folder = "D:\\Face Recognition-Based Attendance System\\register faces\\faces"

known_face_encodings = []
known_face_names = []

# Iterate over the files in the "faces" folder
for filename in os.listdir(faces_folder):
    if filename.endswith(".jpg"):
        student_name = os.path.splitext(filename)[0]
        student_image_path = os.path.join(faces_folder, filename)
        student_image = face_recognition.load_image_file(student_image_path)

        # Check if at least one face is detected in the image
        face_locations = face_recognition.face_locations(student_image)
        if len(face_locations) > 0:
            student_encoding = face_recognition.face_encodings(student_image)[0]
            known_face_encodings.append(student_encoding)
            known_face_names.append(student_name)
        else:
            print(f"No face detected in {student_name}. Skipping.")

# list of expected students
expected_students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Specify the directory for the CSV file
csv_directory = "D:\\Face Recognition-Based Attendance System\\attendance files"

# Create the directory if it doesn't exist
if not os.path.exists(csv_directory):
    os.makedirs(csv_directory)

# Construct the CSV file path
csv_file_path = os.path.join(csv_directory, f"{current_date}.csv")

# Open CSV file for writing
with open(csv_file_path, "w+", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Time", "Date"])


    present_students = []

    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                # add text if a person is present
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                thickness = 3
                fontColor = (255, 0, 0)
                lineType = 2
                cv2.putText(frame, name + " present", bottomLeftCornerOfText, font, fontScale, fontColor, thickness,
                            lineType)

                # update list of present students
                if name in expected_students and name not in present_students:
                    present_students.append(name)
                    current_time = now.strftime("%H:%M:%S")
                    writer.writerow([name, current_time, current_date])

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    print("Present students:", present_students)

# Remaining code for sending SMS to absent students
from twilio.rest import Client



# get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# open CSV file for reading
with open(csv_file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    present_students = [row[0] for row in reader]

# get absent students
absent_students = set(expected_students) - set(present_students)

from twilio.rest import Client



# get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# open CSV file for reading
with open(csv_file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    present_students = [row[0] for row in reader]

# get absent students
absent_students = set(expected_students) - set(present_students)


# Twilio account SID and auth token
account_sid = 'AC21df40dcd70ca289bb8aaf454cd6cdb7'
auth_token = '2af0798adc14bfff9f32861d12ae021d'
client = Client(account_sid, auth_token)

# Read the phone numbers from the text file
students = {}
with open("phone_numbers.txt", "r") as file:
    for line in file:
        name, phone_number = line.strip().split(",")
        students[name] = phone_number

# Remaining code for sending SMS to absent students
# ...

# send text messages to absent students
for student in absent_students:
    to_number = students.get(student)
    if to_number:
        message = client.messages.create(
            body=f"Dear {student}, you were absent on {current_date}. Please contact the teacher.",
            from_="+15392123701",
            to=to_number
        )
        print(f"Text message sent to {student} with SID: {message.sid}")
    else:
        print(f"No phone number found for {student}. Skipping sending message.")