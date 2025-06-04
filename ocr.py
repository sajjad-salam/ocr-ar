import cv2
import pytesseract
from PIL import Image
import numpy as np


def extract_arabic_text(image_path: str) -> str:
    """
    Extracts Arabic text from an image using pytesseract.
    Args:
        image_path (str): Path to the image file.
    Returns:
        str: Extracted Arabic text.
    """
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Optional: Apply thresholding for better OCR results
    # _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Set pytesseract to use the Arabic language
    custom_config = r'-l ara --psm 6'

    # Run OCR on the image
    text = pytesseract.image_to_string(gray, config=custom_config)
    return text


if __name__ == "__main__":
    image_path = 'image.png'
    extracted_text = extract_arabic_text(image_path)
    print('Extracted Arabic Text:')
    print(extracted_text)
