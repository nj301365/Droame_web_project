Droame Web Project
A web-based application designed to manage bookings and drone service requests. This project uses Flask for the backend, MySQL for data persistence, and Bootstrap for a responsive user interface.

🚀 Features
Landing Page: An interactive interface for users to explore services.

Booking System: Integrated modals and forms to capture user requirements.

Database Integration: Securely stores leads and booking information in a MySQL database.

Responsive Design: Built with Bootstrap to ensure compatibility across mobile and desktop devices.

🛠️ Tech Stack
Backend: Python (Flask)

Frontend: HTML5, CSS3, JavaScript, Jinja2

UI Framework: Bootstrap 4.x

Database: MySQL

Environment: Virtualenv

📋 Prerequisites
Before running the project, ensure you have the following installed:

Python 3.9+

MySQL Server

pip (Python package manager)

🔧 Installation & Setup
Clone the Repository

Bash
git clone <repository-url>
cd Droame_web_project
Set Up Virtual Environment

Bash
python -m venv myenv
# Activate on Windows:
myenv\Scripts\activate
# Activate on macOS/Linux:
source myenv/bin/activate
Install Dependencies

Bash
pip install -r requirements.txt
Database Configuration

Open MySQL and create a database named droame_db (or as specified in your app.py).

Update the database credentials in app.py:

Python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database_name'
Run the Application

Bash
python app.py
The app will be available at http://127.0.0.1:5000/.

📁 Project Structure
Plaintext
├── app.py              # Main Flask application entry point
├── requirements.txt    # List of Python dependencies
├── static/             # CSS, JavaScript, and Image assets
├── templates/          # HTML templates (index.html, modal.html, etc.)
└── myenv/              # Python virtual environment (ignored in git)

🤝 Contributing
Fork the project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.
