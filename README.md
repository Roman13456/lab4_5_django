# TV Program Guide Project

This is a Django web application for managing and displaying a TV program guide.

## Features

*   View a list of TV channels.
*   View details for a specific channel, including its programs.
*   View a list of all TV programs.
*   CRUD operations for Channels and Programs.
*   User registration and authentication.

## Setup

Follow these steps to get the project up and running on your local machine.

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Roman13456/lab4_5_django.git
    cd lab4_5_django
    ```

2.  **Create a virtual environment:**

    ```bash
    # Using venv
    python -m venv venv
    # Activate the virtual environment
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    # source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt 
    ```

4.  **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for accessing the Django admin site):**

    ```bash
    python manage.py createsuperuser
    ```

## Running the Project

1.  **Activate your virtual environment** (if not already active).
2.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

3.  Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure

*   `tvprogram_project/`: The main project directory containing settings, URLs, etc.
*   `tvguide/`: The main application for the TV guide functionality.
    *   `models.py`: Defines the database models (Channel, Program).
    *   `forms.py`: Defines forms for handling user input.
    *   `views.py`: Contains the logic for handling requests and rendering templates.
    *   `urls.py`: Defines URL patterns for the app.
    *   `templates/tvguide/`: HTML templates for the TV guide app.
    *   `migrations/`: Database migration files.
*   `templates/registration/`: Templates for user authentication (login, register, logout).
*   `manage.py`: Django's command-line utility.
*   `db.sqlite3`: The default SQLite database file (ignored by Git if added to .gitignore).
*   `.gitignore`: Specifies intentionally untracked files that Git should ignore.
