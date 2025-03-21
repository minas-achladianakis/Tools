from pdf2image import convert_from_path
from PIL import Image
import os

# Get user input
task_number = input("Give me the number of the task: ")
pdf_name = f'My_Work{task_number}.pdf'
output_pdf_name = f'Protected{task_number}.pdf'

# Convert PDF to images
try:
    images = convert_from_path(pdf_name)
except FileNotFoundError:
    print(f"❌ File '{pdf_name}' not found.")
    exit(1)

# Save each page as an image
for idx, img in enumerate(images, start=1):
    img.save(f'image_{idx}.jpg', 'JPEG')

# Prepare images for PDF output
image_list = [
    Image.open(f'image_{i}.jpg').convert('RGB')
    for i in range(2, len(images) + 1)
]

first_image = Image.open('image_1.jpg').convert('RGB')
first_image.save(output_pdf_name, save_all=True, append_images=image_list)

print(f"✅ PDF saved as '{output_pdf_name}'")

# Optional: Clean up temporary images
# for i in range(1, len(images) + 1):
#     os.remove(f'image_{i}.jpg')

