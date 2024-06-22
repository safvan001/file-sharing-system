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

## Deployment
**To deploy the application on AWS EC2:**
  - Set up an EC2 instance with the necessary configurations.
  - Install required software and dependencies on the EC2 instance.
  - Clone the repository and set up the environment.
  - Configure the database and other environment variables.
  - Run the application using a production server like Gunicorn.
  - Set up a reverse proxy using Nginx for better performance and security

**Postman Dump**
  ```bash
  https://documenter.getpostman.com/view/27994184/2sA3XWbyR8



   

   
   
