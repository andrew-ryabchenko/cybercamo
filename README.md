# Cybercamo - LSB Steganography Web App

## Introduction

This Django web application is designed for performing LSB (Least Significant Bit) steganography, a technique for hiding information within digital images. In this application, users can embed and extract payloads from images.

## Features

- **Embed Payloads**: Hide text or binary data inside images without perceptible changes.
- **Extract Payloads**: Retrieve hidden information from images.
- **User-Friendly Interface**: Easy-to-use web interface for all operations.

## Technology Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript

## Installation

You can try this app at [cybercamo.pythonanywhere.com](https://cybercamo.pythonanywhere.com) or run it locally by performing the following steps

1. Clone the repository:
   ```
   git clone [your-repository-link]
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Start the Django server:
   ```
   python manage.py runserver
   ```

## Usage

- **Embedding Data**:
  1. Navigate to the 'Embed' section.
  2. Upload an image and the data to be hidden.
  3. Submit to embed the data and download the modified image.

- **Extracting Data**:
  1. Navigate to the 'Extract' section.
  2. Upload an image with hidden data.
  3. Submit to extract the hidden data.

## Contributing

Contributions, issues, and feature requests are welcome!
