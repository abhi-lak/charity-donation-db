Donation Management System

Overview

The Donation Management System is a Python-based application that facilitates the management of donations and receivers using a MySQL database. It allows users to add, view, update, and delete donation and receiver records efficiently.

Features

Add, update, and delete donor and receiver records

Store donation amounts and track distributions

Retrieve and display records from the database

User-friendly command-line interface

Secure database connection using MySQL

Prerequisites

Ensure you have the following installed before running the project:

Python 3.x

MySQL Server

Required Python packages (install using requirements.txt)

Installation

Clone the repository:

git clone https://github.com/yourusername/donation-management.git
cd donation-management

Install dependencies:

pip install -r requirements.txt

Set up the MySQL database:

Create a new database in MySQL

Update the database connection details in config.py

Run the provided SQL script (if any) to initialize tables

Usage

Run the script using the following command:

python donation_system.py

Follow the on-screen prompts to manage donors and receivers.

Configuration

Update config.py with your MySQL credentials:

DB_HOST = 'your_host'
DB_USER = 'your_user'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database'

Contribution

Feel free to fork this repository, make improvements, and submit a pull request. Contributions are welcome!

License

This project is licensed under the MIT License.

Contact

For any questions or suggestions, contact Abhishek Iyer at aiyer084@gmail.com
