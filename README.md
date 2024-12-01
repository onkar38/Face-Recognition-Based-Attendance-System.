Face Recognition-Based Attendance System Overview This project is an innovative Face Recognition-Based Attendance System designed to streamline attendance management for educational institutions. Developed using Python and OpenCV, the system automates attendance tracking through facial recognition, ensuring accuracy, efficiency, and reliability. The project was awarded First Prize in a Project-Based Learning (PBL) competition during my first year of engineering.

Features Automated Attendance Recording: Recognizes faces in real-time and marks attendance. User-Friendly Interface: Built with Tkinter for easy operation. Data Storage and Reporting: Stores attendance records in Excel for seamless management and reporting. Absentee Notifications: Integrated with Twilio API to send SMS alerts to absentees. Portable and Flexible: Operates on devices powered by portable power banks, making it highly deployable. Technology Stack Programming Language: Python Libraries: OpenCV: For face detection and recognition NumPy: For numerical computations Tkinter: For the GUI interface Twilio: For SMS integration Tools: Microsoft Excel How It Works Face Registration:

Capture and register students' faces into the database. Real-Time Recognition:

The system detects faces using OpenCV and matches them with the registered database. Attendance Marking:

Matches found faces with the database and records their attendance in an Excel sheet. Absentee Notifications:

Sends SMS alerts to absentees via the Twilio API. Portability:

Can be deployed on portable devices with a power bank for maximum flexibility. Installation Prerequisites Python 3.x Libraries: OpenCV NumPy Twilio Tkinter Setup Instructions Clone the repository:

bash Copy code git clone (https://github.com/onkar38/Face-Recognition-Based-Attendance-System/tree/main)
cd face-recognition-attendance
Install dependencies:

bash Copy code pip install -r requirements.txt
Configure Twilio:

Set up a Twilio account. Add your account SID, Auth Token, and phone number in the configuration file. Run the application:

bash Copy code python main.py
Project Structure graphql Copy code face-recognition-attendance/
│
├── database/ # Stores registered face data
├── attendance/ # Stores Excel attendance records
├── main.py # Main application script
├── gui.py # GUI interface code
├── requirements.txt # Required libraries
└── README.md # Project documentation
Acknowledgment This project was guided by Mr. Makrand Kulkarni and developed during my first year of engineering.

License This project is licensed under the MIT License. Feel free to use, modify, and distribute the code for your projects.

Contributing Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and create a pull request.

Contact If you have questions or want to collaborate on future projects, feel free to reach out:

Email: [onkarphopase026@gmail.com] LinkedIn: [https://www.linkedin.com/in/onkar-phopase-62324b259]
