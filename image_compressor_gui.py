# Import the Image module from Pillow
from PIL import Image
# Import PySimpleGUI
import PySimpleGUI as sg

# Define the layout of the GUI
layout = [
    [sg.Text("Choose an image file to compress:")],
    [sg.Input(key="-IN-"), sg.FileBrowse()],
    [sg.Text("Choose the compression ratio (0.1 - 1.0):")],
    [sg.Slider(range=(0.1, 1.0), default_value=0.9, resolution=0.01, orientation="h", key="-RATIO-")],
    [sg.Text("Choose the compression quality (1 - 100):")],
    [sg.Slider(range=(1, 100), default_value=90, resolution=1, orientation="h", key="-QUALITY-")],
    [sg.Button("Compress"), sg.Button("Exit")]
]

# Create the window object
window = sg.Window("Image Compressor", layout)

# Event loop
while True:
    event, values = window.read()
    # If user closes window or clicks Exit
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    # If user clicks Compress
    elif event == "Compress":
        # Get the input values
        image_name = values["-IN-"]
        new_size_ratio = values["-RATIO-"]
        quality = values["-QUALITY-"]
        # Load the image file
        img = Image.open(image_name)
        # Print the original image size
        print("Original size:", img.size)
        # Convert the quality to an integer
        quality = int (quality)

        # Save the compressed image with JPEG format and quality
        img.save("compressed.jpg", format="JPEG", quality=quality, optimize=True)
        # Resize the image with the new size ratio
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.LANCZOS)
        # Save the resized image with JPEG format and quality
        img.save("resized.jpg", format="JPEG", quality=quality, optimize=True)
        # Show a popup message
        sg.popup("Image compressed successfully!")

# Close the window
window.close()
