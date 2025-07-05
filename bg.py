from rembg import remove
from PIL import Image
import os
import io

def removeBackground(inputPath, outputPath=None, showResult=True):
    """
    Removes background from an image using rembg and saves the result as PNG.

    Parameters:
    - inputPath (str): Path of the input image.
    - outputPath (str): Path to save the output image.
    - showResult (bool): If True, shows the result after saving.
    """

    # Check if the file exists
    if not os.path.exists(inputPath):
        print("Error: File not found -", inputPath)
        return

    # Read image in binary
    with open(inputPath, "rb") as file:
        imageData = file.read()

    # Remove background
    try:
        print("Removing background from image...")
        resultData = remove(imageData)
    except Exception as error:
        print("Failed to remove background:", error)
        return

    # Convert to image
    try:
        resultImage = Image.open(io.BytesIO(resultData))
    except Exception as error:
        print("Error converting result to image:", error)
        return

    # Set default output path
    if outputPath is None:
        baseName = os.path.splitext(inputPath)[0]
        outputPath = baseName + "NoBackground.png"

    # Save the result
    try:
        resultImage.save(outputPath)
        print("Background removed. Saved to:", outputPath)
    except Exception as error:
        print("Error saving image:", error)
        return

    # Optionally show the result
    if showResult:
        resultImage.show()


# -----------------------------------
# Example Usage
# -----------------------------------
if __name__ == "__main__":
    inputImage = "myPhoto.jpg"         # Replace with your image name
    outputImage = "myPhotoNoBG.png"    # Optional: where to save the result

    removeBackground(inputImage, outputImage)
