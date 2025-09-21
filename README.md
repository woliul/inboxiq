# InboxIQ

**InboxIQ** is a powerful, offline solution for managing your emails. By converting a standard `.mbox` file into a searchable, filterable, and dashboard-style database, this system gives you full control over your email data without relying on external services.

This project is ideal for anyone who needs to quickly find information in old emails, analyze their email history, or simply access their data in a clean, structured way.

## 💡 Key Features

  - **Offline Access**: Your entire email database is stored locally on your machine.
  - **Powerful Search**: Quickly find emails based on subject, sender, body content, or even custom extracted fields.
  - **Advanced Filtering**: Filter your emails by specific criteria like phone numbers, names, or other data points you define.
  - **Dashboard View**: Get a high-level overview of your emails in a clean, table-based interface.
  - **Full Data Control**: Your data remains yours; no cloud uploads or third-party access is required.

## ⚙️ How It Works

The system operates in three main phases, leveraging Python to transform raw email data into a structured and interactive database.

### 1\. Parsing the `.mbox` File

The process begins by using Python's built-in `mailbox` library to read and process the `.mbox` file. This script iterates through each email, extracting essential data like the **subject**, **sender**, and **body content**.

A key part of this phase is **data extraction**. Using regular expressions, the parser can identify and pull out specific information (e.g., names, phone numbers) from the email body, turning unstructured text into valuable, searchable fields.

### 2\. Storing Data in a Database

Once parsed, the extracted email data is stored in a structured database. **SQLite** is the recommended choice for this project due to its serverless, file-based nature and seamless integration with Python.

A table is created with columns designed to store the parsed data, including a unique `message_id`, `subject`, `sender`, `body_text`, and any custom extracted fields like `extracted_name` or `extracted_phone`.

### 3\. Building the User Interface

A lightweight web framework, such as **Flask** or **Django**, is used to create a local, browser-based user interface. This front-end connects to the SQLite database to:

  - **Display a Dashboard**: Presenting a list of emails in a clean, tabular format.
  - **Enable Filtering & Search**: Allowing users to dynamically query the database based on their input.
  - **Provide a Detailed View**: Showing the full content of an email, with a convenient option to copy the body text.

## 🚀 Getting Started

To get started with InboxIQ, you'll need a `.mbox` file and a Python environment. The project is designed to be self-contained and easy to set up.

### Prerequisites

  - Python 3.x
  - A `.mbox` file (most email clients, like Thunderbird or Apple Mail, can export emails in this format)

### Installation

1.  Clone this repository:

    ```bash
    git clone https://github.com/yourusername/InboxIQ.git
    cd InboxIQ
    ```

2.  Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the parsing script to create your database:

    ```bash
    python parse_mbox.py path/to/your/emails.mbox
    ```

4.  Start the web application:

    ```bash
    python run_app.py
    ```

5.  Open your browser and navigate to `http://127.0.0.1:5000` to access the InboxIQ dashboard.

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for new features, improvements, or bug fixes, please open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
