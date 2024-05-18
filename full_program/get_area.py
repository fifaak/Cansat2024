import math

def get_gsd(sensor_width, working_distance, focal_length, image_width):
    return (sensor_width * working_distance) / (focal_length * image_width)

def get_area(gsd, image_width, image_height, off_nadir_angle):
    """
    Calculates the total area captured by a camera with a given GSD, image resolution, and off-nadir angle.

    Args:
        gsd: Ground Sampling Distance (e.g., in meters/px).
        image_width: Number of pixels in image width.
        image_height: Number of pixels in image height.
        off_nadir_angle: Off-nadir angle in degrees.

    Returns:
        Total area captured by the camera (in same units as GSD squared).
    """

    # Convert off-nadir angle to radians
    radians = math.radians(off_nadir_angle)
    
    # Calculate the actual ground distance accounting for the off-nadir angle
    gsd_along = gsd / math.cos(radians)
    gsd_cross = gsd / math.cos(radians)

    # Calculate area per pixel
    area_per_pixel = gsd_along * gsd_cross

    # Calculate total area covered
    total_area = area_per_pixel * image_width * image_height

    return total_area