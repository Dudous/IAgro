import gps
import time

# Define the port to read GPS data from
port = "/dev/ttyACM0"  # Or your GPS module's port
gps_d = gps.gps(port, debug=True)

try:
    while True:
        # Wait for GPS data to be available
        gps_d.wait_for_data()

        # Get latitude, longitude, altitude, and time
        latitude = gps_d.position_data.latitude
        longitude = gps_d.position_data.longitude
        altitude = gps_d.position_data.altitude
        timestamp = gps_d.position_data.time

        # Print the data to the console
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Altitude: {altitude}")
        print(f"Timestamp: {timestamp}")
        print("-------------------")
        time.sleep(1) # Check for data every second

except KeyboardInterrupt:
    print("Exiting script.")
    # Clean up resources (optional)
