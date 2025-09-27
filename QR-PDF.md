# Make QR Codes Clickable In PDFs

This Python script automates the process of detecting QR codes in a PDF and adding clickable hyperlinks to them. Designed to be user-friendly with a simple GUI for selecting files, it ensures QR codes in PDFs are easily accessible via clickable links at the same time scanable also retains Original Quality of the PDF .

---

## Features

- 🚀 **QR Code Detection**: Uses `pyzbar` to detect QR codes in PDF pages.
- 🔗 **Clickable Hyperlinks**: Automatically inserts clickable hyperlinks corresponding to QR codes.
- 📝 **PDF Processing**: Retains the original PDF layout and content.
- 📂 **Simple File Selection**: Provides a GUI to select the PDF file to process.

---

## Installation

Ensure you have Python installed on your system. Then, install the required dependencies:

```bash
pip install pymupdf pyzbar opencv-python numpy
```

---

## Usage

1. 🛠️ Run the script in IDLE

2. 📑 Select a PDF file using the GUI file dialog.

3. ✅ The script will process the file, detect QR codes, and save a new PDF with clickable links in the same directory. The output file will be named `<original_filename>_with_links.pdf`.

---

## Script Details

### `main.py`
This is the main script that:

- 📖 **Opens a PDF** using `PyMuPDF`.
- 🖼️ **Renders each page** as an image for QR detection.
- 🔍 **Detects QR codes** using `pyzbar`.
- 📐 **Calculates coordinates** for each QR code in the PDF.
- ✏️ **Inserts hyperlinks** for detected QR codes back into the PDF.
  
---

## Acknowledgments

- 📘 **PyMuPDF** for PDF rendering and manipulation.
- 📷 **Pyzbar** for QR code detection.
- 🖌️ **OpenCV** for image processing.

