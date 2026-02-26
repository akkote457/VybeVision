# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 14:35:15 2026

@author: Anoop Kote
"""

"""
pixels_to_csv.py
----------------
Reads every image in a folder and saves pixel stats to a CSV file.
One row per image.

Usage:
    python pixels_to_csv.py
"""

import cv2
import os
import csv

folder = input("Paste your image folder path: ").strip().strip('"')

if not os.path.exists(folder):
    print("Can't find that folder.")
    input("Press Enter to close.")
    exit()

extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
images = [f for f in os.listdir(folder) if f.lower().endswith(extensions)]

if not images:
    print("No images found.")
    input("Press Enter to close.")
    exit()

# Output CSV path
csv_path = os.path.join(folder, "pixel_data.csv")

print(f"\nFound {len(images)} images. Processing...\n")

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)

    # Header row
    writer.writerow([
        "filename",
        "width",
        "height",
        "total_pixels",
        "min_pixel",
        "max_pixel",
        "avg_pixel",
        "std_pixel",
    ])

    for filename in images:
        path = os.path.join(folder, filename)
        img  = cv2.imread(path)

        if img is None:
            print(f"  SKIP  {filename}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape

        writer.writerow([
            filename,
            w,
            h,
            w * h,
            int(gray.min()),
            int(gray.max()),
            round(float(gray.mean()), 2),
            round(float(gray.std()), 2),
        ])

        print(f"  OK    {filename}")

print(f"\nDone. Saved to: {csv_path}")
input("\nPress Enter to close.")