from get_area_pixel import GET_PIXEL
from get_area import get_area, get_gsd
import matplotlib.pyplot as plt
import webbrowser
import qrcode
import numpy as np

image_path = "sample/image.png"
model_path = "old_model.h5"
threshold = 0.23
altitude = 500  # meter
gsd = get_gsd(4.15, altitude, 2.8, 1080)  # mm/px converted to m/px
image_width = 1080
image_height = 1080
off_nadir_angle = 30
latitude = 11.5550497
longitude = 100.55983165

def open_google_earth(lat, lon, alt=0):
    # Construct the URL
    url = f"https://earth.google.com/web/@{lat},{lon},{13000000+alt}a"
    # Open the URL in the default web browser
    webbrowser.open(url)
open_google_earth(latitude, longitude, altitude)

# Get the oil spill area in pixels and the image with contours
OIL_SPILL_PIXEL, OUTPUT_IMG = GET_PIXEL(image_path=image_path, model_path=model_path, threshold_=threshold)
OIL_SPILL_PIXEL *= 4.21875  # Multiply by the scale factor

# Calculate the oil spill area
OIL_SPILL_AREA = get_area(gsd, 1, OIL_SPILL_PIXEL, off_nadir_angle)

# Generate the QR code
url = f"https://earth.google.com/web/@{latitude},{longitude},{13000000+altitude}a"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")

# Convert QR code image to numpy array
qr_img = qr_img.convert("RGB")
qr_array = np.array(qr_img)

# Plot the results
fig, ax = plt.subplots(1, 2, figsize=(15, 10))

# Display the image with the oil spill segmentation
ax[0].imshow(OUTPUT_IMG / 255.0)  # Normalize to [0, 1] for display
ax[0].set_title(f"Oil Spill Segmentation (Threshold = {threshold})\n Oil Spill Area: {OIL_SPILL_AREA} m² (approximately)\n lat:{latitude}, lon:{longitude}")
ax[0].axis('off')

# Display the QR code
ax[1].imshow(qr_array)
ax[1].set_title("Google Earth Location QR Code")
ax[1].axis('off')

plt.show()
