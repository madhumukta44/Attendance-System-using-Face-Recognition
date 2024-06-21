# Attendance-System-using-Face-Recognition

A Flask-based web application for managing attendance through face recognition.

## Features

- User authentication (login/signup)
- Face recognition for attendance
- Attendance record keeping
- Responsive web design

## Technologies Used

- Flask (Python)
- HTML/CSS
- JSON for data storage
- Face recognition libraries

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- Werkzeug (for password hashing)
- Any additional libraries mentioned in requirements.txt

### Installation

1. Clone the repository:

    bash
    git clone https://github.com/your-username/attendance-management-system.git
    cd attendance-management-system
    

2. Create a virtual environment and activate it:

    bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

3. Install the required packages:

    bash
    pip install -r requirements.txt
    

4. Set up the data directory:

    Ensure you have a static/data directory with a user_data.json file. The structure should look like this:

    json
    {
        "users": [],
        "login_details": {}
    }
    

### Running the Application

1. Start the Flask application:

    bash
    python app.py
    

2. Open your web browser and go to http://127.0.0.1:5000/attendance/login to access the application.

## Usage

### Login

1. Navigate to the login page: http://127.0.0.1:5000/attendance/login
2. Enter your user ID and password to log in.

### Signup

1. Navigate to the signup page: http://127.0.0.1:5000/attendance/signup
2. Fill in the registration form and submit to create a new account.

### Take Attendance

1. After logging in, select the section for which you want to take attendance.
2. Follow the prompts to start the attendance process using face recognition.
