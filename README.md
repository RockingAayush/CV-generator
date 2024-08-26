# Django CV Generator

This Django project allows users to create professional resumes by entering their details into a form, selecting from pre-designed templates, and downloading their customized CV in PDF format.

## Features

- **Data Entry Form:** Users can fill in their personal and professional details.
- **Template Selection:** Users can choose from multiple CV templates.
- **PDF Generation:** The selected CV template is rendered into a PDF and made available for download.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/RockingAayush/CV-generator.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd django-cv-generator
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/` to use the CV Generator.

## Usage

1. **Fill Out the Form:**
   - Navigate to the form at `http://127.0.0.1:8000/accept/`.
   - Enter your name, email, phone number, and other details.
   - Submit the form to save your information.

2. **Select a Template:**
   - After submitting the form, you'll be directed to the template selection page.
   - Choose from one of the available templates.

3. **Download Your CV:**
   - The selected template will be rendered as a PDF.
   - The PDF will be automatically downloaded to your device.

## Project Structure

- **views.py:** Contains the logic for handling form submission, template selection, and PDF generation.
- **models.py:** Defines the `Profile` model used to store user information.
- **templates/pdf:** Contains the HTML templates for the different CV designs.
- **urls.py:** Maps URLs to the appropriate views.

## PDF Generation

This project uses [pdfkit](https://pypi.org/project/pdfkit/) for rendering HTML templates as PDF files. Ensure that `wkhtmltopdf` is installed on your system.


## Acknowledgments

- This project is inspired by the need to create a quick and easy solution for generating professional resumes.
- Special thanks to the Django and pdfkit communities for their tools and resources.

