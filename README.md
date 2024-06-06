# Password Strength Checker

## Description

The Password Strength Checker is a web application designed to evaluate the strength of user-inputted passwords in real-time. It uses a combination of frontend technologies (HTML, CSS, JavaScript) and a backend powered by Python and Flask. The application provides immediate feedback on password strength based on criteria such as length, use of uppercase and lowercase letters, numbers, and special characters.

## Features

- Real-time password strength evaluation
- Visual indicators of password strength
- Criteria-based strength assessment (length, uppercase, lowercase, numbers, special characters)
- User-friendly interface with HTML and CSS
- Backend logic implemented with Python and Flask

## Project Structure

password_checker/

├── app.py

├── templates/

│ └── index.html

├── static/

│ ├── css/

│ │ └── style.css

│ ├── js/

│ │ └── script.js


## Setup and Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the Repository:**

   ```sh
   gh repo clone hariharasudhanr391/Password-Strength-Checker
   cd password_checker
1. **Install Dependencies:**

   ```sh
   pip install Flask

### Running the Application
1. **Run the Flask Application:**

   ```sh
   python app.py
2. **Open your web browser and navigate to**
     ```sh
   http://127.0.0.1:5000/

## Usage

1. Enter a password into the input field.
2. The application will evaluate the password in real-time and display the strength.
   - **Too short**: Password is less than 6 characters.
   - **Weak**: Password is between 6 and 8 characters.
   - **Fair**: Password meets at least 3 of the criteria (uppercase, lowercase, numbers, special characters) but is less than 12 characters.
   - **Good**: Password meets at least 3 criteria and is at least 8 characters long.
   - **Strong**: Password meets at least 3 criteria and is 12 or more characters long.



## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.
