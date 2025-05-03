import exifread
import requests
import os
import json
import argparse
from datetime import datetime
##### CREATED BY MORTUJA MONDAL for fun #####
def dms_to_decimal(dms, ref):
    degrees = float(dms[0].num) / float(dms[0].den)
    minutes = float(dms[1].num) / float(dms[1].den)
    seconds = float(dms[2].num) / float(dms[2].den)
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_exif(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)
    return tags

def get_location(lat, lon):
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=10"
        headers = {"User-Agent": "ImageOSINT/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("display_name", "Location not found")
    except requests.exceptions.RequestException as e:
        return f"Error retrieving location: {e}"

def parse_args():
    parser = argparse.ArgumentParser(description="Image Metadata Extractor (EXIF OSINT Tool)")
    parser.add_argument('-f', '--file', required=True, help="Path to the image file (e.g., JPG, JPEG)")
    return parser.parse_args()

def main():
    args = parse_args()
    sample_image = args.file

    if not os.path.isfile(sample_image):
        print(f"Error: File '{sample_image}' does not exist.")
        return

    print("\nProcessing image...\n")
    tags = extract_exif(sample_image)

    if not tags:
        print("No metadata found in the image.")
        return

    # 1. Device & Camera Info
    print("Device & Camera Info:")
    device_keys = ['Image Make', 'Image Model', 'Image Device', 'Image Manufacturer']
    found = False
    for key in device_keys:
        if key in tags:
            print(f"  {key.split()[-1]}: {tags[key]}")
            found = True
    if not found:
        print("  - No device info found.")

    # 2. Date/Time Info
    print("\nDate/Time Info:")
    time_keys = ['EXIF DateTimeOriginal', 'Image DateTime', 'EXIF DateTimeDigitized']
    found = False
    for key in time_keys:
        if key in tags:
            print(f"  {key.split()[-1]}: {tags[key]}")
            found = True
    if not found:
        print("  - No timestamp info found.")

    # 3. Software Info
    print("\nSoftware Info:")
    software_keys = ['Image Software', 'EXIF Software', 'Image Application', 'PDF Producer']
    found = False
    for key in software_keys:
        if key in tags:
            print(f"  {key.split()[-1]}: {tags[key]}")
            found = True
    if not found:
        print("  - No software info found.")

    # 4. Image Information
    print("\nImage Information:")
    image_keys = ['EXIF DateTimeOriginal', 'Image Orientation', 'Image ResolutionUnit', 'Image XResolution', 'Image YResolution']
    found = False
    for key in image_keys:
        if key in tags:
            print(f"  {key.split()[-1]}: {tags[key]}")
            found = True
    if not found:
        print("  - No image info found.")

    # 5. Exposure Settings
    print("\nExposure Settings:")
    exposure_keys = ['EXIF ExposureTime', 'EXIF FNumber', 'EXIF Flash', 'EXIF ISOSpeedRatings']
    found = False
    for key in exposure_keys:
        if key in tags:
            print(f"  {key.split()[-1]}: {tags[key]}")
            found = True
    if not found:
        print("  - No exposure settings found.")

    # 6. GPS Info
    print("\nGPS Location Info:")
    if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
        try:
            lat = dms_to_decimal(tags["GPS GPSLatitude"].values, tags["GPS GPSLatitudeRef"].printable)
            lon = dms_to_decimal(tags["GPS GPSLongitude"].values, tags["GPS GPSLongitudeRef"].printable)
            address = get_location(lat, lon)
            print(f"  Latitude: {lat}")
            print(f"  Longitude: {lon}")
            print(f"  Address: {address}")
        except Exception as e:
            print(f"  Error processing GPS data: {e}")
    else:
        print("  - No GPS data found.")

if __name__ == '__main__':
    main()

