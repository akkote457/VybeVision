# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 14:08:10 2026

@author: Anoop Kote
"""

"""
gray_batch.py
-------------
Grays every image in a folder and saves them to a new folder called "grayed".

Usage:
    python gray_batch.py

Then just paste in the folder path when it asks.
"""

import cv2
import os

# Ask for folder
folder = input("Paste your image folder path: ").strip().strip('"')

if not os.path.exists(folder):
    print("Can't find that folder.")
    input("Press Enter to close.")
    exit()

# Create output folder
output_folder = os.path.join(folder, "grayed")
os.makedirs(output_folder, exist_ok=True)

# Supported image types
extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

# Get all image files
images = [f for f in os.listdir(folder) if f.lower().endswith(extensions)]

if not images:
    print("No images found in that folder.")
    input("Press Enter to close.")
    exit()

print(f"\nFound {len(images)} images. Processing...\n")

success = 0
failed  = 0

for filename in images:
    path = os.path.join(folder, filename)
    img  = cv2.imread(path)

    if img is None:
        print(f"  SKIP  {filename}")
        failed += 1
        continue

    gray     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    out_path = os.path.join(output_folder, filename)
    cv2.imwrite(out_path, gray)
    print(f"  OK    {filename}")
    success += 1

print(f"\nDone. {success} grayed, {failed} skipped.")
print(f"Saved to: {output_folder}")
input("\nPress Enter to close.")