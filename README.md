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
   git clone https://github.com/your-username/exif-metadata-extractor.git
   cd exif-metadata-extractor
