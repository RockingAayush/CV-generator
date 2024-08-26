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
    cd CV-generator
    ```

3. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Start the development server:**

    ```bash
    python manage.py runserver
    ```

5. **Access the application:**

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
Since wkhtmltopdf needs to be added to path, you'll need to install it manually. Here’s how you can do that:

- **Download the appropriate wheel file for wkhtmltopdf:**

    Visit a website like https://github.com/JazzCore/python-pdfkit for installation details, or download the .whl file from a trusted source.
- **Install the wheel file:**

    ```bash
    pip install /path/to/your/wkhtmltopdf.whl
    ```
- **Ensure wkhtmltopdf is available on your system's PATH:**

*Windows*
- Right-click on "This PC" or "My Computer" and select "Properties."
- Click on "Advanced system settings."
- Click on "Environment Variables."
- Under "System variables," find the PATH variable and click "Edit."
- Add the path to the directory where wkhtmltopdf.exe is located.

*Linux/macOS*
- You can add wkhtmltopdf to your PATH by editing your shell configuration file (~/.bashrc, ~/.zshrc, etc.):

```bash
export PATH="/path/to/wkhtmltopdf:$PATH"
```
  
- After adding it to the PATH, run source ~/.bashrc or source ~/.zshrc to apply the changes.
## Acknowledgments

- This project is inspired by the need to create a quick and easy solution for generating professional resumes.
- Special thanks to the Django and pdfkit communities for their tools and resources.

