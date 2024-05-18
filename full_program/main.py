from get_area_pixel import  GET_PIXEL
from get_area import get_area,get_gsd


image_path = "sample/image.png"
model_path = "old_model.h5"
threshord = 0.23
OIL_SPILL_PIXEL = GET_PIXEL(image_path=image_path, model_path=model_path, threshold_=threshord) * 4.21875
height = 50  # meter
gsd = get_gsd(4.15, height, 2.8, 1080)  # mm/px converted to m/px
image_width = 1080
image_height = 1080
off_nadir_angle = 30

print(f"Total area covered: {get_area(gsd, 1, OIL_SPILL_PIXEL, off_nadir_angle):.6f} m² (approximately)")