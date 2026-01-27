# Password Manager (Tkinter GUI)

A simple Password Manager desktop application built using Python and Tkinter.
It allows users to generate strong random passwords and store website credentials locally.
This project required significant time and effort to complete, particularly in understanding Tkinter’s grid layout, event-driven logic, and integrating password generation with the GUI workflow.


## Features

- Generates strong random passwords using letters, numbers, and symbols
- Automatically inserts generated passwords into the password field
- Saves website, email/username, and password to a local file
- Input validation using pop-up alerts
- Confirmation dialog before saving credentials


## Technologies Used

- Python 3
- Tkinter

## Project Structure

Day29/
- logo.png
- data.txt
- main.py

## How It Works

- The Generate Password button creates a random password and inserts it into the password entry field
- The Add button checks for empty fields, shows a confirmation dialog, and saves the data to data.txt


## Future Improvements

- Copy password to clipboard
- Store credentials in JSON format
- Encrypt stored passwords
- Improve UI design

## Learning Outcomes

- Understanding Tkinter grid layout
- Event-driven programming in Python
- GUI application development
- File handling with user confirmation dialogs
