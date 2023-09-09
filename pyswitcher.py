import sys
from openrgb import OpenRGBClient

def load_openrgb_profile(profile_name):
    try:
        client = OpenRGBClient()
        client.load_profile(profile_name)
        print(f"Profile '{profile_name}' loaded successfully!")
    except FileNotFoundError:
        print(f"Error: Profile '{profile_name}' not found.")
    except ConnectionError:
        print("Error: Unable to connect to OpenRGB. Make sure it's running.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <profile_name>")
        sys.exit(1)

    desired_profile = " ".join(sys.argv[1:])
    load_openrgb_profile(desired_profile)
    