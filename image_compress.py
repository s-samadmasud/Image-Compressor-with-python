# Import the Image module from Pillow
from PIL import Image

# Load the image file
img = Image.open("AI NEWS PRESENTER 2.jpg")

# Print the original image size
print("Original size:", img.size)

# Save the compressed image with JPEG format and quality 80
img.save("compressed1.jpg", format="JPEG", quality=60, optimize=True)
