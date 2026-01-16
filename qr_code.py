import qrcode

# The data you want to encode in the QR code (e.g., a website URL, text, etc.)
data_to_encode = "https://aadityabhilegaonkar.netlify.app/" 

# Create an instance of the QRCode class
# - version: controls the size of the QR Code (None means it is automatically chosen)
# - error_correction: controls the error correction features (L, M, Q, H)
# - box_size: controls how many pixels each 'box' or 'module' of the QR code is
# - border: controls how many boxes thick the border should be
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add the data to the QR code object
qr.add_data(data_to_encode)
qr.make(fit=True)

# Create an image from the QR code object
# You can change the colors here (fill_color is the dark part, back_color is the background)
img = qr.make_image(fill_color="black", back_color="white")

# Save the image file
# This will save the image in the same folder where you run the script.
filename = "qrcode.png"
img.save(filename)

print(f"QR Code generated and saved as {filename}!")
#