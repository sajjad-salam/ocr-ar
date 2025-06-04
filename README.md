# Arabic OCR using pytesseract

This project extracts Arabic text from images using Python, OpenCV, and pytesseract.

## Requirements

- Python 3.x
- Tesseract-OCR (with Arabic language data)
- Python packages (see `requirements.txt`)

## Installation

1. Install Tesseract-OCR:
   - Windows: Download from [UB Mannheim builds](https://github.com/UB-Mannheim/tesseract/wiki) and install. Make sure to add Tesseract to your PATH.
   - Install Arabic language data (usually included, or run: `tesseract --list-langs` to check).
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   for linux users, you may need to install tesseract using your package manager, e.g., `sudo apt install tesseract-ocr tesseract-ocr-ara`.
3. Ensure you have the Arabic language data for Tesseract. You can check available languages with:
   ```bash
   tesseract --list-langs
   ```

## Usage

1. Place your image file (e.g., `image.png`) in the project directory.
2. Run the script:
   ```bash
   python ocr.py
   ```
3. The extracted Arabic text will be printed to the console.

## Notes

- For best results, use high-quality images with clear Arabic text.
- You can adjust preprocessing steps in the script for different image types.

## License

This project is provided for educational purposes.
