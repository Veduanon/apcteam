from PIL import Image

# Load the image (change 'your_image.png' to the path of your image)
img = Image.open('Abstraction.png').convert('L')  # Convert to grayscale ('L' mode)

# Extract brightness values along the diagonal
diagonal_brightness = [img.getpixel((i, i)) for i in range(min(img.size))]

result = []
# Append the brightness values for each pixel along the diagonal
for brightness in diagonal_brightness:
    result.append(str(brightness))  # Convert each brightness value to a string

# Join the list of strings into one string separated by spaces and then split (optional)
text = ''

for i in result:

    text += i + ' '


