from get_area_pixel import GET_PIXEL
from get_area import get_area, get_gsd
import matplotlib.pyplot as plt

image_path = "sample/image.png"
model_path = "old_model.h5"
threshold = 0.23

# Get the oil spill area in pixels and the image with contours
OIL_SPILL_PIXEL, OUTPUT_IMG = GET_PIXEL(image_path=image_path, model_path=model_path, threshold_=threshold)
OIL_SPILL_PIXEL *= 4.21875  # Multiply by the scale factor

# Example parameters for get_area and get_gsd
height = 50  # meter
gsd = get_gsd(4.15, height, 2.8, 1080)  # mm/px converted to m/px
image_width = 1080
image_height = 1080
off_nadir_angle = 30

# Calculate the oil spill area
OIL_SPILL_AREA = get_area(gsd, 1, OIL_SPILL_PIXEL, off_nadir_angle)

# Display the image with the oil spill segmentation
plt.figure(figsize=(10, 10))
plt.imshow(OUTPUT_IMG / 255.0)  # Normalize to [0, 1] for display
plt.title(f"Oil Spill Segmentation (Threshold = {threshold}), Oil Spill Area: {OIL_SPILL_AREA} m² (approximately)")
plt.axis('off')
plt.show()
