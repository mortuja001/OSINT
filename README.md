# 📸 EXIF Metadata Extractor (Image OSINT Tool)

A simple Python-based command-line tool to extract and analyze EXIF metadata from images. This project is inspired by real-world Open Source Intelligence (OSINT) techniques used in image forensics.

---

## 🔍 Features

- Extracts and categorizes metadata into:
  - 📱 Device & Camera Info
  - 🕒 Date/Time stamps
  - 🧠 Software used
  - 🖼️ Image settings (resolution, orientation, etc.)
  - ⚙️ Exposure settings (ISO, Flash, Aperture)
  - 🌍 GPS data with **reverse geolocation lookup**

- Uses `argparse` for easy CLI usage
- Lightweight and dependency-minimal
- Ideal for forensic analysts, OSINT learners, and privacy researchers

---

## 🚀 How to Use::
### 🔧 Installation

Ensure you have Python 3 installed.

1. Clone the repo:
   ```bash
   git clone https://github.com/MortujaMondal/OSINT
   cd OSINT
## 🌍 Reverse Geolocation
###  The tool uses the OpenStreetMap Nominatim API to convert GPS coordinates into human-readable locations:
    -https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=10
## ❓Why Nominatim?
  -Free and open-source
  -No API key required
  -Respects user privacy
  -Ideal for offline or privacy-conscious forensics
  -APIs like Google Maps or Bing Maps were avoided due to key management, quota limits, and privacy concerns.

##📦 Dependencies
 -exifread – For reading EXIF tags
 -requests – For performing HTTP requests to Nominatim
 -argparse – Built-in module for CLI

Install them using:
  --pip install exifread requests

---
Reference:

---
