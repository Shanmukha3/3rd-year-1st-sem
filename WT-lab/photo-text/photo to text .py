import pytesseract
from PIL import Image

# Define the Tesseract executable path (replace with your actual path)
pytesseract.pytesseract.tesseract_cmd = r'CProgram FilesTesseract-OCRtesseract.exe'

# Load the image using Pillow
image = Image.open('img.png')

# Perform OCR on the image
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print(extracted_text)
