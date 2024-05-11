# Universal-Notepad
A webserver that has a notepad that anyone can edit
# Flask Text Editor

A simple text editor web application built using Flask. This application enables users to write and save text into a file, then retrieve and edit it as needed. The application loads the text from a file into the web interface and provides the ability to modify and save changes back to the file.

## Features
- **Load Text**: Reads text data from a local file and displays it in the web interface.
- **Edit and Save**: Allows editing of text and saves changes to the file upon form submission.
- **Web-based UI**: Uses Flask templates to provide a simple and user-friendly web interface.

## Getting Started

### Prerequisites
- Python 3.x
- Flask

### Installation
1. Clone the repository or download the project files.
2. Navigate to the project directory and install the required dependencies using pip:

    ```bash
    pip install flask
    ```

3. Create a `text_data.txt` file in the project directory to store the text data:

    ```bash
    touch text_data.txt
    ```

### Usage
1. Start the Flask server by running:

    ```bash
    python app.py
    ```

2. Access the application by visiting `http://127.0.0.1:5000/` in your web browser.

3. Enter or modify text in the editor and submit to save changes.

### Project Structure
- `app.py`: Main application script containing the routes and logic.
- `text_data.txt`: File used to store the text data.
- `templates/index.html`: HTML template for the web interface.

### Contribution Guidelines
1. Fork the repository and create a new branch for your feature or bug fix.
2. Make your changes and submit a pull request with a detailed description of your modifications.
3. Ensure your changes are consistent with the project's style and aim.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

