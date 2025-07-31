# Excel Search App

A simple Flask web application to upload Excel files and search for any value across all columns in a selected file. Matching rows are displayed in a table.

---

## Features

- **Upload Excel files** (`.xlsx`) to the server.
- **Search for any value** across all columns in a selected Excel file.
- **View all matching rows** in a table.
- Duplicate file upload is prevented with a clear error message.
- Temporary Excel files (starting with `~$`) are ignored.

---

## How It Works

1. **Uploading Excel Files**
    - Use the upload form to add `.xlsx` files.
    - Duplicate filenames are not allowed; you’ll see an error if you try to upload a file that already exists.
    - Uploaded files are stored in the `uploads` folder.

2. **Searching in Excel Files**
    - Select an uploaded file and enter a value to search.
    - The app searches all columns for the value (case-insensitive).
    - All matching rows are shown in a table.
    - The search value remains in the input box after searching.

---

## Usage

## Installation & Running

1. **Create a virtual environment:**
    ```
    python -m venv env
    ```

2. **Activate the virtual environment:**
    ```
    env\Scripts\activate
    ```

3. **Install required packages:**
    ```
    pip install flask pandas openpyxl
    ```

4. **Save dependencies:**
    ```
    pip freeze > requirements.txt
    ```

5. **(Optional) Install dependencies from requirements.txt:**
    ```
    pip install -r requirements.txt
    ```

6. **Run the Flask app:**
    ```
    python app.py
    ```

7. **Open your browser and go to:**
    ```
    http://127.0.0.1:5000/
    ```

3. **Open your browser:**  
   Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

4. **Upload and search:**
    - Upload an Excel file using the form.
    - Select a file and enter a value to search.
    - View results in the table.

---

## Project Structure

```
excel_search_app/
│
├── app.py
├── uploads/                # Uploaded Excel files are stored here
└── templates/
    └── index.html          # Main HTML template
```

---

## Requirements

- Python 3.x
- Flask
- pandas
- Werkzeug

---

## Notes

- Only `.xlsx` files are supported.
- Make sure to close Excel files before uploading if you plan to overwrite them.
- Temporary Excel files (starting with `~$`) are ignored.

---

## License

MIT License
