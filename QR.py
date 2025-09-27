import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
import os

# Suppress internal zbar warnings
os.environ["PYTHONWARNINGS"] = "ignore"

def read_existing_links(file_name):
    try:
        with open(file_name, 'r') as file:
            return set(file.read().splitlines())
    except FileNotFoundError:
        return set()

def save_link(file_name, link):
    with open(file_name, 'a') as file:
        file.write(link + '\n')

def main():
    file_name = 'links.txt'
    existing_links = read_existing_links(file_name)
    seen_links = set()

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set fixed resolution
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Decode only QR codes
        for code in decode(frame, symbols=[ZBarSymbol.QRCODE]):
            link = code.data.decode('utf-8')

            if link not in existing_links:
                print(f"New Link Found: {link}")
                existing_links.add(link)
                save_link(file_name, link)
            elif link not in seen_links:
                print(f"Duplicate Link: {link}")
                seen_links.add(link)

        cv2.imshow('QR Code Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
