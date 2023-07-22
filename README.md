# Assignment Submission and Feedback System

The Assignment Submission and Feedback System is a web application built using Django, a Python web framework. The system provides a platform for students to submit their assignments, lecturers to post assignments, and facilitate discussions between students and lecturers. This README file provides a comprehensive guide to understanding and using the system.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
  - [Creating a User Account](#creating-a-user-account)
  - [Logging In](#logging-in)
  - [User Profile](#user-profile)
  - [Viewing All Submitted Assignments](#viewing-all-submitted-assignments)
  - [Posting an Assignment](#posting-an-assignment)
  - [Posting a Discussion](#posting-a-discussion)
  - [Viewing and Marking Assignments (Lecturers)](#viewing-and-marking-assignments-lecturers)
  - [Viewing All Marked Assignments (Lecturers)](#viewing-all-marked-assignments-lecturers)
  - [Viewing Discussions](#viewing-discussions)
  - [Viewing All Discussions](#viewing-all-discussions)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

To run the Assignment Submission and Feedback System on your local machine, you will need the following installed:

- Python (version 3.x)
- Django (version 3.x)
- Virtualenv (recommended)

### Installation

1. Clone the repository to your local machine using the following command:

```
git clone https://github.com/Levi-Chinecherem/assignment-submission-system.git
```

2. Navigate to the project directory:

```
cd assignment-submission-system
```

3. Create a virtual environment (optional but recommended):

```
python -m venv venv
```

4. Activate the virtual environment:

- Windows:

```
venv\Scripts\activate
```

- macOS / Linux:

```
source venv/bin/activate
```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Apply the database migrations:

```
python manage.py migrate
```

7. Create a superuser to access the Django admin interface:

```
python manage.py createsuperuser
```

8. Start the development server:

```
python manage.py runserver
```

The Assignment Submission and Feedback System should now be up and running at `http://localhost:8000/`.

## Features

The Assignment Submission and Feedback System offers the following features:

- User registration and authentication
- Profile management (for users to provide additional information)
- Assignment submission by students
- Assignment posting by lecturers
- Discussions on assignments and other topics
- Assignment marking by lecturers

## Usage

### Creating a User Account

To use the system, users need to create an account:

1. Access the home page at `http://localhost:8000/`.
2. Click on "Sign Up" to register a new account.
3. Provide the required information and click on "Sign Up."

### Logging In

After creating an account, users can log in:

1. Access the home page at `http://localhost:8000/`.
2. Click on "Login."
3. Enter your username and password and click "Login."

### User Profile

After logging in, users can update their profiles with additional information:

1. Click on "Profile" in the navigation bar.
2. Update the profile details and click "Save Profile."

### Viewing All Submitted Assignments

Students can view all their submitted assignments:

1. Click on "Submitted Assignments" in the navigation bar.

### Posting an Assignment

Lecturers can post assignments:

1. Click on "Post Assignment" in the navigation bar.
2. Fill in the assignment details and click "Submit."

### Posting a Discussion

Lecturers and students can post discussions:

1. Click on "Post Discussions" in the navigation bar.
2. Fill in the discussion details and click "Submit."

### Viewing and Marking Assignments (Lecturers)

Lecturers can view assignments and mark them:

1. Click on "Mark Assignments" in the navigation bar.
2. View the details of each assignment and provide the total score.
3. Click "Submit" to mark the assignment.

### Viewing All Marked Assignments (Lecturers)

Lecturers can view all marked assignments:

1. Click on "Marked Assignments" in the navigation bar.

### Viewing Discussions

Users can view discussions:

1. Click on "Join Discussions" in the navigation bar.
2. Click on a discussion to view its details.

### Viewing All Discussions

Users can view all discussions:

1. Click on "All Discussions" in the navigation bar.

## Contributing

If you would like to contribute to the Assignment Submission and Feedback System, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your forked repository.
4. Create a pull request to the main repository.

We appreciate any contributions and feedback!

## License

The Assignment Submission and Feedback System is open-source software released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.


This README provides an overview of the Assignment Submission and Feedback System and guides users on how to use the system's features. If you have any questions or need further assistance, feel free to contact the project maintainers or me directly. Enjoy using the system!