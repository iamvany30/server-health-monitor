# Server Health Monitor

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-1.1.2-orange)](https://flask.palletsprojects.com/)
[![CEF Python](https://img.shields.io/badge/CEF_Python-66.0-green)](https://github.com/cztomczak/cefpython)

## Overview

The **Server Health Monitor** is a web application designed to provide real-time metrics on server health such as CPU usage, disk usage, memory usage, total processes, and server status. The backend is powered by Flask, serving data to a frontend built with modern CSS and JavaScript. Additionally, the application can be embedded in a desktop environment using the Chromium Embedded Framework (CEF).

## Features

- Real-time monitoring of critical server metrics.
- Responsive and visually appealing design.
- Graceful fallback for users without JavaScript.
- Regular updates every 10 seconds.
- Desktop application mode using CEF.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.9 installed on your machine.
- `pip` installed (Python package manager).
- Basic knowledge of Python, HTML, CSS, and JavaScript.

## Installation

### Clone the Repository

Clone the repository to your local machine using Git.

### Set Up Virtual Environment (Optional but Recommended)

It's recommended to use a virtual environment to manage dependencies.

### Install Dependencies

Install the required Python packages from the `requirements.txt` file.

### Configure Static Files

Ensure that static files (`styles.css`, `script.js`) are correctly placed in the `/static/index/` directory relative to your Flask application's root.

## Usage

### Start the Application

Run the Flask server to start serving the application.

### Access the Application

Open your web browser and navigate to the specified URL to access the Server Health Monitor dashboard.

### Desktop Application Mode

For running the application as a desktop application using CEF, just run SHMonitor

## File Structure

The project follows a standard structure with directories for the main application, static files, and templates.

## Contributing

We welcome contributions! Please fork the repository, create a new branch, commit your changes, push to the branch, and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please reach out to us via email at [iamvany@vk.com].

---
