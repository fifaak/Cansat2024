import webbrowser

def open_google_earth(latitude, longitude, altitude=0):
    """
    Opens Google Earth at the specified coordinates and altitude.

    Args:
        latitude (float): The latitude in degrees (north is positive).
        longitude (float): The longitude in degrees (east is positive).
        altitude (int, optional): The zoom level (0 is farthest out, higher numbers zoom in). Defaults to 0.

    Raises:
        ValueError: If latitude or longitude is outside the valid range.
    """

    # Validate latitude and longitude values
    if not (-90 <= latitude <= 90):
        raise ValueError("Latitude must be between -90 and 90 degrees.")
    if not (-180 <= longitude <= 180):
        raise ValueError("Longitude must be between -180 and 180 degrees.")

    # Construct the URL with proper formatting
    url = f"https://earth.google.com/web/@{latitude},{longitude},{altitude}a"

    # Open the URL in the default web browser
    webbrowser.open(url)

# Example usage (assuming you have latitude and longitude values)
try:
    open_google_earth(37.7833, -122.4167,1000)  # Example coordinates for San Francisco
except ValueError as e:
    print(f"Error: {e}")
