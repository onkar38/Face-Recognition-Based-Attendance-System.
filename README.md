# Face-Recognition-Based Attendance System

This system automates attendance tracking using real-time face detection and recognition. By capturing and recognizing faces from a camera feed, it accurately logs attendance with timestamps and exports the data for easy reporting and analysis. This project is ideal for use in classrooms, labs, and small offices.

## Features

  * **Real-time Attendance:** Automatically detects and recognizes faces from a live camera feed.
  * **Simple Workflow:** Follows a straightforward three-step process: **Enrollment** → **Training** → **Attendance**.
  * **Scalable Design:** Handles multiple faces in a single frame, making it suitable for group settings.
  * **Flexible Data Export:** Logs attendance with timestamps directly to **CSV** or **Excel** files.
  * **Modular Architecture:** The system's design is highly maintainable and easy to extend.

## Architecture

The system follows a conventional, three-stage pipeline for face recognition.

1.  **Enrollment:** Images of each person are captured from a webcam and saved to the `TrainingImages/` directory. For best results, capture 30–100 images per person from different angles and lighting conditions.
2.  **Training:** The system processes the captured images to compute face encodings (embeddings) and saves them as a serialized model (e.g., a `.pkl` or `.npz` file) in the `models/` folder. This model is used for recognition.
3.  **Recognition:** During an attendance session, the system detects faces in each frame, computes their encodings, and compares them to the trained model using a distance threshold. It logs each person's attendance once per session to prevent duplicate entries.

The final attendance logs are stored in the `attendance/` directory, typically with a new file created per day or session (e.g., `YYYY-MM-DD_subject.csv`).

## Tech Stack

  * **Language:** Python 3.9+
  * **Core Libraries:** OpenCV for camera access, `dlib` or `face-recognition` for face processing, `NumPy`, and `pandas` for data handling.
  * **UI:** Optional front-ends can be built with **Tkinter** for a desktop application or **Flask** for a web interface.
  * **Data Storage:** **CSV** or **Excel** for logs; **SQLite** can be used for more advanced session management.

-----

## Getting Started

### Prerequisites

  * Python 3.9 or higher
  * `pip` package installer
  * A working webcam or video input
  * **For dlib:** CMake and build tools are required on Windows/macOS.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/onkar38/Face-Recognition-Based-Attendance-System
    cd Face-Recognition-Based-Attendance-System
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Create necessary folders:**
    ```
    TrainingImages/
    models/
    attendance/
    ```

### Usage

1.  **Enroll Users:** Run the enrollment script to capture images for each person. Enter their name/ID, and the system will capture and save 30–100 images.
2.  **Train the Model:** Run the training script to process the images and generate the face encoding model.
3.  **Take Attendance:** Run the attendance script. The system will start recognizing faces and automatically log entries to a CSV file.

## Configuration & Tips for Accuracy

  * **Tuning the Threshold:** Adjust the Euclidean distance threshold (typically between 0.5 and 0.6) to balance between precision (correctly identifying a person) and recall (identifying all people).
  * **High-Quality Images:** Capture a large number of diverse images per person, including different angles, facial expressions, and lighting conditions.
  * **Optimal Environment:** Ensure a well-lit environment and a stable camera position at face level to prevent motion blur and poor-quality images.

## Roadmap & Extensions

  * **Advanced Features:** Implement an admin login, role-based access, and class/subject management.
  * **Notifications:** Integrate with services like **Twilio** or **SendGrid** to send SMS or email alerts on attendance events.
  * **Dashboards:** Create analytics dashboards using tools like **Power BI** or **Streamlit** to visualize attendance trends.
  * **Improved Security:** Add liveness detection to prevent spoofing with photos or videos.

## Contributing

We welcome contributions\! Please open an issue to report bugs or suggest features, and submit pull requests with clear commit messages and updated documentation.

## License

This project is licensed under the **MIT License**.
