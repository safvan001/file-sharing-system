# File Sharing System

## Introduction

This is a secure file-sharing system between two different types of users: Ops Users and Client Users.

## Features

- **Ops User:**
  - Login
  - Upload File (only pptx, docx, and xlsx)

- **Client User:**
  - Sign Up (returns an encrypted URL)
  - Email Verification
  - Login
  - Download File
  - List All Uploaded Files

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/safvan001/file-sharing-system.git
   cd file-sharing-system
2. **Set Up the Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Set Up the Database:**
   ```bash
   python manage.py migrate
5. **Run the Development Server:**
   ```bash
   python manage.py runserver


   

   
   
