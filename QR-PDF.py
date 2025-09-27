import fitz  # PyMuPDF
from pyzbar.pyzbar import decode as pyzbar_decode
import cv2
import numpy as np
import os
from tkinter import Tk, filedialog

def extract_qr_codes_with_pyzbar(image):
    """Detect QR codes using Pyzbar."""
    qr_codes = pyzbar_decode(image)
    results = []
    for qr in qr_codes:
        data = qr.data.decode('utf-8')
        rect = qr.rect
        results.append({"data": data, "rect": rect})
    return results

def add_hyperlinks_to_pdf(input_pdf_path, output_pdf_path):
    """Extract QR codes from the PDF and add hyperlinks."""
    doc = fitz.open(input_pdf_path)
    qr_count = 0

    for page_number in range(len(doc)):
        page = doc[page_number]
        print(f"Processing Page {page_number + 1}...")

        # Render the page as an image
        pix = page.get_pixmap(dpi=300)
        image = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)

        # Convert the image to grayscale for QR detection
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        # Detect QR codes using Pyzbar
        qr_codes = extract_qr_codes_with_pyzbar(gray_image)
        qr_count += len(qr_codes)

        for qr in qr_codes:
            data = qr['data']
            rect = qr['rect']

            # Calculate PDF coordinates for the QR code
            x0 = rect.left * (page.rect.width / pix.width)
            y0 = rect.top * (page.rect.height / pix.height)
            x1 = (rect.left + rect.width) * (page.rect.width / pix.width)
            y1 = (rect.top + rect.height) * (page.rect.height / pix.height)

            # Add a hyperlink annotation to the PDF
            link = {
                "kind": fitz.LINK_URI,  # Specify the link type as URI
                "uri": data,           # Set the hyperlink destination
                "from": fitz.Rect(x0, y0, x1, y1)  # Define the clickable area
            }
            page.insert_link(link)
            print(f"  Added hyperlink for QR code: {data}")

    if qr_count > 0:
        doc.save(output_pdf_path)
        print(f"\nProcessed {qr_count} QR codes and saved output to: {output_pdf_path}")
    else:
        print("\nNo QR codes detected. Output file was not saved.")
    doc.close()

def select_and_process_pdf():
    """GUI for selecting a PDF file and processing it."""
    # Open file dialog
    Tk().withdraw()  # Hide the root Tkinter window
    input_pdf_path = filedialog.askopenfilename(
        title="Select PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not input_pdf_path:
        print("No file selected.")
        return

    # Generate output PDF path
    input_dir, input_filename = os.path.split(input_pdf_path)
    output_filename = os.path.splitext(input_filename)[0] + "_with_links.pdf"
    output_pdf_path = os.path.join(input_dir, output_filename)

    print(f"Processing file: {input_pdf_path}")
    print(f"Saving to: {output_pdf_path}")

    # Process the PDF
    add_hyperlinks_to_pdf(input_pdf_path, output_pdf_path)

if __name__ == "__main__":
    select_and_process_pdf()
