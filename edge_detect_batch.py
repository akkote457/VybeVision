# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 14:31:02 2026

@author: Anoop Kote
"""

"""
edges_batch.py
--------------
Runs edge detection on every image in a folder.
Saves results to an "edges" subfolder.

Usage:
    python edges_batch.py
"""

import cv2
import os

folder = input("Paste your image folder path: ").strip().strip('"')

if not os.path.exists(folder):
    print("Can't find that folder.")
    input("Press Enter to close.")
    exit()

# Create output folder
output_folder = os.path.join(folder, "edges")
os.makedirs(output_folder, exist_ok=True)

extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")
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
    edges    = cv2.Canny(gray, 100, 200)
    out_path = os.path.join(output_folder, filename)
    cv2.imwrite(out_path, edges)
    print(f"  OK    {filename}")
    success += 1

print(f"\nDone. {success} processed, {failed} skipped.")
print(f"Saved to: {output_folder}")
input("\nPress Enter to close.")